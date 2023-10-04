"""
    Describes all colors in RGB format that we create for each occupant
    with variable the maximum amount of shading for each of rgb
"""

import random


class Color:
    """
        Includes:
        -(int) red the fraction of red shade that exists within the color created
        -(int) green the fraction of green shade that exists within the color created
        -(int) blue the fraction of blue shade that exists within the color created
    """

    def __init__(self, maxnum=255):
        # initialized to black
        self.red = 0
        self.green = 0
        self.blue = 0
        self.set_color(maxnum)

    """
        the color might change no matter if it is initialized or not 
    """

    def set_color(self, maxnum=255):
        random.seed(1)
        self.red = random.randint(0, maxnum)
        self.green = random.randint(0, maxnum)
        self.blue = random.randint(0, maxnum)
