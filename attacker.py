"""attacker

Description
===============================

This Python module is for the Ice_Attacker and Temp_Attacker classes.

Copyright and Usage Information
===============================

This file is Copyright (c) 2020 Caleb Sadler.
"""

import pygame
import game_values


class Attacker:
    """Super class for IceAttacker and TempAttacker
         abstract class representing a general attacker
    """
    # Private Instance Attributes:
    # - img: holds this Attacker's image
    # - hyper_speed: fastest speed of the Attacker
    # - fast_speed: medium speed of the Attacker
    # - normal_speed: normal speed of the Attacker
    # - speed: speed at which the Attacker moves toward center
    # - dit: direction of the Attacker
    # - l_w: length and width of Attacker
    # - x: Attacker's current x position
    # - y: Attacker's current y position
    _img: pygame.Surface
    _hyper_speed: float
    _fast_speed: float
    _normal_speed: float
    _speed: float
    _dir: int
    _l_w: float
    _x: float
    _y: float

    def __init__(self, img_path: str, x: float) -> None:
        """Initialize default Attacker"""
        self._img = pygame.image.load(img_path)
        self._hyper_speed = 200.0
        self._fast_speed = 20.0
        self._normal_speed = 2.0
        self._speed = self._normal_speed
        self._l_w = self._img.get_size()[0]
        self._x = x

    def main(self, game_screen: pygame.Surface, vals: dict) -> None:
        """Call all the functions that is needed for Attacker to operate"""
        self.paint(game_screen)
        if not vals['bools']['pausing']:
            self.move()
            self.check_speed(vals)

    def move(self) -> None:
        """Move Attacker to center of screen"""
        self._x += self._speed

    def check_speed(self, vals: dict) -> None:
        """Depending on speed variables, changes the speed of the attackers"""
        if vals['bools']['hyper']:
            self._speed = self._dir * self._hyper_speed
        elif vals['bools']['fast']:
            self._speed = self._dir * self._fast_speed
        else:
            self._speed = self._dir * self._normal_speed

    def paint(self, game_screen: pygame.Surface) -> None:
        """Paint the Attacker on to the screen"""
        game_screen.blit(self._img, (self._x - self._l_w / 2, self._y - self._l_w / 2,
                                     self._l_w, self._l_w))

    def check_destroy(self) -> bool:
        """Return if Attacker should be destroyed (has reached center)"""
        raise NotImplementedError


class IceAttacker(Attacker):
    """Moving Rectangle with image of ice cube

        Ice Attacker will attack the big glacier from the left of the
        screen and delete it self once reached.
    """

    def __init__(self, img_path: str, x: float) -> None:
        """Initialize default Ice Attacker"""
        Attacker.__init__(self, img_path, x)
        self._dir = 1
        self._speed *= self._dir
        self._y = game_values.SCREEN_H / 4 + 50

    def check_destroy(self) -> bool:
        """Return if Ice Attacker should be destroyed (has reached center)"""
        if self._x >= game_values.SCREEN_W / 2:
            return True
        return False


class TempAttacker(Attacker):
    """Moving Rectangle with image of sun

        Temp Attacker (Temperature Attacker) will attack the big thermometer
        from the right of the screen and delete it self once reached.
    """

    def __init__(self, img_path: str, x: float) -> None:
        """Initialize default Temp Attacker"""
        Attacker.__init__(self, img_path, x)
        self._dir = -1
        self._speed *= self._dir
        self._y = 3 * game_values.SCREEN_H / 4 + 50

    def check_destroy(self) -> bool:
        """Return if Temp Attacker should be destroyed (has reached center)"""
        if self._x <= game_values.SCREEN_W / 2:
            return True
        return False


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
