from actions import Action
from territory import Territory
import random


class Revolution(Action):

    def __init__(self, probability, separatist_movement_neighbors, colors_list, occupant_list):
        super().__init__('Revolution', probability)
        self.opponent_is_defeated = False
        self.new_territory = None
        self.separatist_movement_neighbors = separatist_movement_neighbors
        self.colors_list = colors_list
        self.occupant_list = occupant_list

    def run_revolution(self, occupant):
        """
            Selecting a random separatist movement name from the available for
            the given country
        """
        separation = occupant.separatist_movements
        random.seed(1)
        rand_int = random.randint(0, len(separation) - 1)
        movement_name = separation[rand_int]

        # a territory, an occupant and a color with the name given will be created and added to ww database
        self.new_territory = Territory(movement_name, [], self.separatist_movement_neighbors[movement_name])

        print(movement_name, "has revolted against", occupant.name, "and gained its independence")

        # Searching the new occupant's given color and checking if it was given somewhere else before

        for color in self.colors_list:

            # changing the color to a new one if it was given before
            if color == self.new_territory.occupant.color:
                self.new_territory.occupant.color.set_color()

            self.colors_list.append(self.new_territory.occupant.color)

            # the territory has gained its independence
            occupant.remove_separatist_movement(movement_name)

            # adding the new territory as a neighbor to everyone
            new_neighbors = self.new_territory.occupant.neighbors
            for occupant in self.occupant_list:
                if occupant.name in new_neighbors:
                    occupant.add_neighbor(self.new_territory.name)
