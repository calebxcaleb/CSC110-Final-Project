"""paint

Description
===============================

This Python module is for anything related to visuals. It displays colour,
images, text and changes them based on the game state.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

import pygame
import game_values

# Colours
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)
LIGHT_BLUE = (68, 227, 245)
BROWN = (204, 102, 0)


def load_pygame() -> pygame.Surface:
    """Returns pygame screen so other files can access it
        Loads all constants that require pygame
    """
    pygame.init()

    # Set up the drawing window
    global GAME_SCREEN

    GAME_SCREEN = pygame.display.set_mode([game_values.SCREEN_W, game_values.SCREEN_H])
    pygame.display.set_caption('Show Text')

    # The following three functions are declaring global constants in functions.
    # The reason this is done in a function is because these globals require
    # pygame.init() and pygame.init() should only be called once. Instead of
    # calling the pygame.init() outside the function at a moduler level, I
    # called it in a function so that pygame.init() along with the constants
    # that need it would be called once. For this reason there is Py-TA warning
    # but there was no other option.
    load_fonts()
    load_images()
    load_text()

    return GAME_SCREEN


def load_fonts() -> None:
    """Loads all fonts that require pygame"""
    global FONT60
    global FONT45
    global FONT30
    global FONT20
    global FONT15

    FONT60 = pygame.font.Font('freesansbold.ttf', 60)
    FONT45 = pygame.font.Font('freesansbold.ttf', 45)
    FONT30 = pygame.font.Font('freesansbold.ttf', 30)
    FONT20 = pygame.font.Font('freesansbold.ttf', 20)
    FONT15 = pygame.font.Font('freesansbold.ttf', 15)


def load_images() -> None:
    """Loads all images that require pygame"""
    global ICE_IMAGE
    global TEMP_IMAGE
    global ICE_UP_IMAGE
    global ICE_DOWN_IMAGE
    global TEMP_UP_IMAGE
    global TEMP_DOWN_IMAGE

    ICE_IMAGE = pygame.image.load(game_values.ICE_BIG)
    TEMP_IMAGE = pygame.image.load(game_values.TEMP_BIG)
    ICE_UP_IMAGE = pygame.image.load(game_values.ICE_UP)
    ICE_DOWN_IMAGE = pygame.image.load(game_values.ICE_DOWN)
    TEMP_UP_IMAGE = pygame.image.load(game_values.TEMP_UP)
    TEMP_DOWN_IMAGE = pygame.image.load(game_values.TEMP_DOWN)


def load_text() -> None:
    """Loads all text objects that require pygame"""
    # Text - Starting Screen
    global TITLE_TEXT
    global START_BUTTON_TEXT
    global NAME_TEXT

    TITLE_TEXT = FONT60.render('Effect of Climate Change on Sea Ice Extent',
                               True, BLACK, None)
    START_BUTTON_TEXT = FONT60.render('Start', True, BLACK, None)
    NAME_TEXT = FONT60.render('Made by Caleb Sadler', True, BLACK, None)

    # Text - Monthly Data
    global DATE_TEXT
    global ICE_TITLE_TEXT
    global TEMP_TITLE_TEXT

    DATE_TEXT = FONT30.render('Year: Month', True, BLACK, None)
    ICE_TITLE_TEXT = FONT20.render('Ice Data', True, BLACK, None)
    TEMP_TITLE_TEXT = FONT20.render('Temp Data', True, BLACK, None)

    # Text - Legend
    global ICE_UP_TEXT
    global ICE_DOWN_TEXT
    global TEMP_UP_TEXT
    global TEMP_DOWN_TEXT

    ICE_UP_TEXT = FONT20.render(' = +0.5 million square km', True, BLACK, None)
    ICE_DOWN_TEXT = FONT20.render(' = -0.5 million square km', True, BLACK, None)
    TEMP_UP_TEXT = FONT20.render(' = +0.05 degrees celsius', True, BLACK, None)
    TEMP_DOWN_TEXT = FONT20.render(' = -0.05 degrees celsius', True, BLACK, None)

    # Text - Buttons
    global PAUSE_BUTTON_TEXT
    global FAST_BUTTON_TEXT
    global HYPER_BUTTON_TEXT

    PAUSE_BUTTON_TEXT = FONT45.render('Pause', True, BLACK, None)
    FAST_BUTTON_TEXT = FONT45.render('Faster', True, BLACK, None)
    HYPER_BUTTON_TEXT = FONT45.render('Hyper', True, BLACK, None)


def paint(ice_data: list, temp_data: list, vals: dict) -> None:
    """Paint essential images and information to screen"""
    if vals['bools']['starting']:
        GAME_SCREEN.fill(LIGHT_BLUE)
        display_start()
    else:
        GAME_SCREEN.fill(WHITE)
        pygame.draw.rect(GAME_SCREEN, BROWN, game_values.ICE_RECT_PATH)
        pygame.draw.rect(GAME_SCREEN, BROWN, game_values.TEMP_RECT_PATH)
        GAME_SCREEN.blit(ICE_IMAGE, game_values.ICE_BIG_POS)
        GAME_SCREEN.blit(TEMP_IMAGE, game_values.TEMP_BIG_POS)
        display_button(vals)
        display_legend()
        display_monthly_data(ice_data, temp_data, vals)


def display_start() -> None:
    """Display start screen"""
    pygame.draw.rect(GAME_SCREEN, WHITE, game_values.START_BUTTON_RECT)
    pygame.draw.rect(GAME_SCREEN, BLACK, game_values.START_BUTTON_RECT, 10)
    GAME_SCREEN.blit(TITLE_TEXT, game_values.TITLE_TEXT_POS)
    GAME_SCREEN.blit(START_BUTTON_TEXT, game_values.START_BUTTON_TEXT_POS)
    GAME_SCREEN.blit(NAME_TEXT, game_values.NAME_TEXT_POS)


def display_button(vals: dict) -> None:
    """Display game buttons to screen"""
    pygame.draw.rect(GAME_SCREEN, vals['cols']['pause_white'], game_values.PAUSE_BUTTON_RECT)
    pygame.draw.rect(GAME_SCREEN, BLACK, game_values.PAUSE_BUTTON_RECT, 10)

    pygame.draw.rect(GAME_SCREEN, vals['cols']['fast_white'], game_values.FAST_BUTTON_RECT)
    pygame.draw.rect(GAME_SCREEN, BLACK, game_values.FAST_BUTTON_RECT, 10)

    pygame.draw.rect(GAME_SCREEN, vals['cols']['hyper_white'], game_values.HYPER_BUTTON_RECT)
    pygame.draw.rect(GAME_SCREEN, BLACK, game_values.HYPER_BUTTON_RECT, 10)

    GAME_SCREEN.blit(PAUSE_BUTTON_TEXT, game_values.PAUSE_BUTTON_TEXT_POS)
    GAME_SCREEN.blit(FAST_BUTTON_TEXT, game_values.FAST_BUTTON_TEXT_POS)
    GAME_SCREEN.blit(HYPER_BUTTON_TEXT, game_values.HYPER_BUTTON_TEXT_POS)


def display_legend() -> None:
    """Display legend explaining the attacker's real life value"""
    GAME_SCREEN.blit(ICE_UP_IMAGE, (game_values.LEGEND_POS_1[0],
                                    game_values.LEGEND_POS_1[1], 100, 100))
    GAME_SCREEN.blit(ICE_DOWN_IMAGE, (game_values.LEGEND_POS_2[0],
                                      game_values.LEGEND_POS_2[1], 100, 100))
    GAME_SCREEN.blit(TEMP_UP_IMAGE, (game_values.LEGEND_POS_3[0],
                                     game_values.LEGEND_POS_3[1], 100, 100))
    GAME_SCREEN.blit(TEMP_DOWN_IMAGE, (game_values.LEGEND_POS_4[0],
                                       game_values.LEGEND_POS_4[1], 100, 100))

    GAME_SCREEN.blit(ICE_UP_TEXT, game_values.ICE_UP_TEXT_POS)
    GAME_SCREEN.blit(ICE_DOWN_TEXT, game_values.ICE_DOWN_TEXT_POS)
    GAME_SCREEN.blit(TEMP_UP_TEXT, game_values.TEMP_UP_TEXT_POS)
    GAME_SCREEN.blit(TEMP_DOWN_TEXT, game_values.TEMP_DOWN_TEXT_POS)


def display_monthly_data(ice_data: list, temp_data: list, vals: dict) -> None:
    """Display text for main game"""
    # Year and month displayed at top left of screen
    year = vals['date_vals']['year_index'] + game_values.YEAR_ADDER
    now_month = game_values.MONTHS[vals['date_vals']['month_index']]
    new_date_text = FONT30.render(str(year) + ': ' + now_month, True, BLACK, None)
    GAME_SCREEN.blit(new_date_text, game_values.DATA_TEXT_POS)

    # Monthly data displayed on side of towers
    GAME_SCREEN.blit(ICE_TITLE_TEXT, game_values.ICE_TITLE_TEXT_POS)
    GAME_SCREEN.blit(TEMP_TITLE_TEXT, game_values.TEMP_TITLE_TEXT_POS)

    for i in range(0, len(game_values.MONTHS)):
        month = game_values.MONTHS[i]
        ice_value = ice_data[vals['date_vals']['year_index']][i]
        temp_value = temp_data[vals['date_vals']['year_index']][i]

        month_text = FONT20.render(month + ': ' + str(ice_value), True, BLACK, None)
        month_ice_text_pos = (game_values.SCREEN_W / 2 + 200, 200 + 20 * i)
        GAME_SCREEN.blit(month_text, month_ice_text_pos)

        month_text = FONT20.render(month + ': ' + str(temp_value), True, BLACK, None)
        month_temp_text_pos = (game_values.SCREEN_W / 2 + 450, 200 + 20 * i)
        GAME_SCREEN.blit(month_text, month_temp_text_pos)


def paint_flip() -> None:
    """Updates the screen to see changes from painting"""
    pygame.display.flip()


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pygame', 'game_values', 'python_ta.contracts'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
