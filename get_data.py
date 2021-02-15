"""get_data

Description
===============================

This Python module is designed to retrieve data from the datasets and
turn the data into a list separated by year and month. This module will
be called by main.py and the list will be stored in game_values.py.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

import csv
from typing import List
import logging

FILE_PATH = ['datasets/ice_data.csv', 'datasets/temp_data.csv']
ROW_DELETE = [4, 5]
COLUMN_INDEX = [2, 1]
DATA_MAX = 1000
DATA_MIN = 1000


def get_data(n: int) -> List[List[float]]:
    """ Return list of years which are lists of months which represent
        the month's data(temperature or ice)

        when n is 0, the data for sea ice extent will be retrieved
        when n is 1, the data for global temperatures will be retrieved

        Precondition
        - n == 0 or n == 1
    """
    with open(FILE_PATH[n]) as file:
        reader = csv.reader(file)

        # set up initial values
        data_so_far = []
        month = 1
        year = []

        # Skip header rows
        for _ in range(0, ROW_DELETE[n]):
            next(reader)

        # loop through the file
        for row in reader:
            # reset values for the next year
            if month > 12:
                data_so_far.append(year)
                year = []
                month = 1
            # input the given months data
            value = float(row[COLUMN_INDEX[n]])
            if value > DATA_MAX or value < -DATA_MIN:
                value = 0
                # There should be two values that go out of the expected range
                logging.warning("Data set value out of expected range")
            year.append(value)
            month += 1

    return data_so_far


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['game_values', 'logging', 'csv', 'List', 'python_ta.contracts'],
        'allowed-io': ['open'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
