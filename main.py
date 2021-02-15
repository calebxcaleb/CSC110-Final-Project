"""main

Description
===============================

This Python module is for running the project simulation.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

import pygame
import paint
import game_functions
import get_data

# load pygame values and initialize game_screen
GAME_SCREEN = paint.load_pygame()


def game_loop() -> None:
    """Loop for while game is running"""
    # list of current attackers
    attackers = []

    # initialize list of data for ice extent and temperature
    ice_data = get_data.get_data(0)
    temp_data = get_data.get_data(1)

    # booleans for running the game
    bools = {
        'starting': True,
        'running': True,
        'pausing': False,
        'fast': False,
        'hyper': False,
        'can_click': True
    }

    # changing colours for buttons
    cols = {
        'pause_white': paint.WHITE,
        'fast_white': paint.WHITE,
        'hyper_white': paint.WHITE
    }

    # values for changing months and years
    date_vals = {
        'year_index': 0,
        'month_index': 0,
    }

    # dictionary of dictionaries
    vals = {
        'bools': bools,
        'cols': cols,
        'date_vals': date_vals
    }

    # add attacker for the first round
    game_functions.add_attackers(attackers, ice_data, temp_data, vals)

    while bools['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bools['running'] = False
            if event.type == pygame.MOUSEBUTTONUP:
                bools['can_click'] = True

        paint.paint(ice_data, temp_data, vals)
        game_functions.mouse_check(vals)

        if not bools['starting']:
            game_functions.attacker_handler(attackers, ice_data, temp_data,
                                            GAME_SCREEN, vals)

        paint.paint_flip()

    pygame.quit()


if __name__ == '__main__':
    game_loop()
