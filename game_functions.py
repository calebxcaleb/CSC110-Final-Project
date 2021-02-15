"""game_functions

Description
===============================

This Python module is for managing the game functions. It manages all the attackers
by calling their main methods, the buttons by calculating collisions with the buttons
and doing their respective tasks.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

from typing import Tuple
import pygame
import game_values
import paint
from attacker import IceAttacker, TempAttacker


###########################################
#               Attackers                 #
###########################################
def attacker_handler(attackers: list, ice_data: list, temp_data: list,
                     game_screen: pygame.Surface, vals: dict) -> None:
    """Handle any operations for the attackers"""
    for i in range(0, len(attackers)):
        attackers[i].main(game_screen, vals)
        if attackers[i].check_destroy():
            attackers.pop(i)
            break

    if attackers == []:
        if vals['date_vals']['year_index'] < game_values.YEAR_MAX and \
           vals['date_vals']['month_index'] >= game_values.MONTH_MAX:
            vals['date_vals']['year_index'] += 1
            vals['date_vals']['month_index'] = 0
        else:
            vals['date_vals']['month_index'] += 1
        add_attackers(attackers, ice_data, temp_data, vals)


def add_attackers(attackers: list, ice_data: list, temp_data: list, vals: dict) -> None:
    """Once attackers list is empty, adds new set of attackers based on the next month"""
    if vals['date_vals']['year_index'] < len(ice_data) and \
            vals['date_vals']['month_index'] < len(ice_data[0]):
        # Adding Ice Attackers
        ice_info = calculate_attacker_info(0, 2, ice_data, vals)

        for i in range(0, ice_info[0]):
            attackers.append(IceAttacker(ice_info[1], i * -100))

        # Adding Temp Attackers
        temp_info = calculate_attacker_info(1, 20, temp_data, vals)

        for i in range(0, temp_info[0]):
            attackers.append(TempAttacker(temp_info[1], game_values.SCREEN_W + i * 100))
    else:
        game_values.running = False


def calculate_attacker_info(n: int, multiplier: int, data: list, vals: dict)\
        -> Tuple[int, str]:
    """calculate the amount and type(positive or negative) of attackers to add

        Precondition
        - n == 0 or n == 1
        - multiplier > 0
        - data == game_values.ice_data or data == game_values.temp_data
    """
    if data[vals['date_vals']['year_index']][vals['date_vals']['month_index']] < 0:
        img_path = game_values.IMAGES[n][2]
    else:
        img_path = game_values.IMAGES[n][1]

    attack_num = int(abs(data[vals['date_vals']['year_index']]
                         [vals['date_vals']['month_index']]) * multiplier)

    return (attack_num, img_path)


###########################################
#               Input                     #
###########################################
def pause_button_handler(vals: dict) -> None:
    """Handles operations for when 'pause' button is pressed"""
    if vals['bools']['can_click']:
        vals['bools']['pausing'] = not vals['bools']['pausing']
        vals['bools']['can_click'] = False
        if vals['bools']['pausing']:
            vals['cols']['pause_white'] = paint.GRAY
        else:
            vals['cols']['pause_white'] = paint.WHITE


def fast_button_handler(vals: dict) -> None:
    """Handles operations for when 'faster' button is pressed"""
    if vals['bools']['can_click']:
        vals['bools']['can_click'] = False
        if vals['bools']['fast']:
            vals['bools']['fast'] = False
            vals['cols']['fast_white'] = paint.WHITE
        else:
            vals['bools']['fast'] = True
            vals['bools']['hyper'] = False
            vals['cols']['fast_white'] = paint.GRAY
            vals['cols']['hyper_white'] = paint.WHITE


def hyper_button_handler(vals: dict) -> None:
    """Handles operations for when 'hyper' button is pressed"""
    if vals['bools']['can_click']:
        vals['bools']['can_click'] = False
        if vals['bools']['hyper']:
            vals['bools']['hyper'] = False
            vals['cols']['hyper_white'] = paint.WHITE
        else:
            vals['bools']['hyper'] = True
            vals['bools']['fast'] = False
            vals['cols']['hyper_white'] = paint.GRAY
            vals['cols']['fast_white'] = paint.WHITE


def collision(rect: Tuple[float, float, float, float]) -> bool:
    """Return whether mouse position collides with given rectangle area"""
    if rect[0] < pygame.mouse.get_pos()[0] < rect[0] + rect[2] and \
       rect[1] < pygame.mouse.get_pos()[1] < rect[1] + rect[3]:
        return True
    return False


def mouse_check(vals: dict) -> None:
    """Handle mouse clicks"""
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if vals['bools']['starting'] and collision(game_values.START_BUTTON_RECT):
            vals['bools']['starting'] = False
        elif collision(game_values.PAUSE_BUTTON_RECT):
            pause_button_handler(vals)
        elif not vals['bools']['pausing']:
            if collision(game_values.FAST_BUTTON_RECT):
                fast_button_handler(vals)
            if collision(game_values.HYPER_BUTTON_RECT):
                hyper_button_handler(vals)


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pygame', 'game_values', 'paint', 'Tuple', 'attacker',
                          'IceAttacker', 'TempAttacker', 'python_ta.contracts'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
