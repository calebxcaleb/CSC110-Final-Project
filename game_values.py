"""game_values

Description
===============================

This Python module is for global variables and allowing other modules
to access them from one place.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

########################
# Game values
########################
SCREEN_W = 1400
SCREEN_H = 800
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
YEAR_ADDER = 1979
YEAR_MAX = 40
MONTH_MAX = 11

########################
# Image Paths
########################
ICE_BIG = 'images/ice_big.png'
ICE_UP = 'images/ice_up.png'
ICE_DOWN = 'images/ice_down.png'
TEMP_BIG = 'images/temp_big.png'
TEMP_UP = 'images/temp_up.png'
TEMP_DOWN = 'images/temp_down.png'
ICE_IMAGES = [ICE_BIG, ICE_UP, ICE_DOWN]
TEMP_IMAGES = [TEMP_BIG, TEMP_UP, TEMP_DOWN]
IMAGES = [ICE_IMAGES, TEMP_IMAGES]

########################
# Rectangle Positions
########################
START_BUTTON_RECT = (SCREEN_W / 2 - 90, 400, 180, 90)
PAUSE_BUTTON_RECT = (SCREEN_W - 600, 25, 160, 70)
FAST_BUTTON_RECT = (SCREEN_W - 400, 25, 160, 70)
HYPER_BUTTON_RECT = (SCREEN_W - 200, 25, 160, 70)

ICE_RECT_PATH = (0, SCREEN_H / 4, SCREEN_W / 2, 100)
TEMP_RECT_PATH = (SCREEN_W / 2, 3 * SCREEN_H / 4, SCREEN_W / 2, 100)

########################
# X-Y positions
########################
ICE_BIG_POS = (SCREEN_W / 2 - 150, SCREEN_H / 4 - 150)
TEMP_BIG_POS = (SCREEN_W / 2 - 150, 3 * SCREEN_H / 4 - 150)

LEGEND_POS_1 = (100, SCREEN_H / 2 - 50)
LEGEND_POS_2 = (100, SCREEN_H / 2 + 50)
LEGEND_POS_3 = (100, SCREEN_H / 2 + 150)
LEGEND_POS_4 = (100, SCREEN_H / 2 + 250)

TITLE_TEXT_POS = (SCREEN_W / 2 - 625, 80)
START_BUTTON_TEXT_POS = (START_BUTTON_RECT[0] + 15, START_BUTTON_RECT[1] + 15)
NAME_TEXT_POS = (SCREEN_W / 2 - 325, 200)

DATA_TEXT_POS = (100, 75)
ICE_TITLE_TEXT_POS = (SCREEN_W / 2 + 200, 150)
TEMP_TITLE_TEXT_POS = (SCREEN_W / 2 + 450, 150)

ICE_UP_TEXT_POS = (200, SCREEN_H / 2)
ICE_DOWN_TEXT_POS = (200, SCREEN_H / 2 + 100)
TEMP_UP_TEXT_POS = (200, SCREEN_H / 2 + 200)
TEMP_DOWN_TEXT_POS = (200, SCREEN_H / 2 + 300)

PAUSE_BUTTON_TEXT_POS = (PAUSE_BUTTON_RECT[0] + 12, PAUSE_BUTTON_RECT[1] + 12)
FAST_BUTTON_TEXT_POS = (FAST_BUTTON_RECT[0] + 12, FAST_BUTTON_RECT[1] + 12)
HYPER_BUTTON_TEXT_POS = (HYPER_BUTTON_RECT[0] + 12, HYPER_BUTTON_RECT[1] + 12)

if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
