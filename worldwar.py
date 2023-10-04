"""
    Bootleg WorldWarBot with existing countries and the most popular separatist movements 
    from the past and present from all over the world. No typical alliances between any country. 
"""

from revolution import Revolution
from portal import Portal
from conquest import Conquest
from territory import Territory
import random


class WorldWar:
    """
        WorldWar is the most important class in the bot. It really is the core of the program
        that starts and runs the bot. It includes:
        -(int) num_of_countries, the number of countries existing
        -(list of class territory) territory_list, the territories existing
        -(list of class occupant) occupant_list, the countries remaining
        -(list of class colors) colors_list, the colors existing in the map
        -(dictionary with class occupant keys and list of class territory) neighbors_dict
        a dictionary with each occupant and its neighbor's territories
        -(dictionary with class occupant keys and list of strings) separatist_movements
        a dictionary with each occupant and the names of separatist movements happening
        in its territories
        These are the stuff that will go on in the world war
    """

    def __init__(self, countries_list, separatist_movements, neighbor_dictionary, separatist_movements_neighbors):

        # the starting number of countries fighting
        self.num_of_countries = len(countries_list)

        """
            initializing all class lists
        """
        self.territory_list = []
        self.occupant_list = []
        self.colors_list = []

        """
            initializing each fighting country as a territory and an occupant and writing to the list its color
        """
        for name in countries_list:

            territory = Territory(name, separatist_movements[name], neighbor_dictionary[name])
            self.territory_list.append(territory)

            """
                Searching the occupant's given color and checking if it was given somewhere else before
            """
            for color in self.colors_list:

                # changing the color to a new one if it was given before
                if color == territory.occupant.color:
                    territory.occupant.color.set_color()

            self.occupant_list.append(territory.occupant)
            self.colors_list.append(territory.occupant.color)
            self.separatist_movements_neighbors_dict = {}

            # Initializing each separatist movement's potential neighbor list

            for movement in separatist_movements_neighbors:
                self.separatist_movements_neighbors_dict[movement] = []

                # Adding neighbor territories for each separatist movement in the respective lists

            for movement in self.separatist_movements_neighbors_dict:

                new_neighbors = self.separatist_movements_neighbors_dict[movement]

                """
                    Searching the territory list for each separatist movement's neighbor in order
                    to add each corresponding neighbor territory to the new dictionary
                """
                for neighbor in new_neighbors:

                    for territory in self.territory_list:

                        # We found the territory
                        if territory.name == neighbor:
                            self.separatist_movements_neighbors_dict[movement].append(territory)

        # We create a conquest action, a portal action, and a revolution action
        self.conquest = Conquest(0.8)
        self.revolution = Revolution(
            0.2, self.separatist_movements_neighbors_dict,
            self.colors_list,
            self.occupant_list
        )
        self.portal = Portal(self.conquest.probability / 80, self.territory_list)

    def run(self):
        """
            WWBOT runs in this function
            separatist_movements_neighbors is a dictionary with key a separatist movement name 
            and lists of territory names as values. In the beginning of the run function, we will
            create a dictionary with the separatist movement names as keys and lists of territories 
            as values
        """

        # Selecting a random country to affect their result in the war
        random.seed(1)
        rand_int = random.randint(0, len(self.occupant_list) - 1)
        occupant = self.occupant_list[rand_int]

        """
            Deciding which of the possible actions will happen by seeding.
            If the seed is less or equal than the possibility of a revolution
            happening in the run, then a separatist movement will happen. Otherwise,
            a conquest of a territory will happen
        """
        seed = random.random()

        # A separatist movement will happen
        if seed <= self.revolution.probability:

            self.revolution.run_revolution(occupant)

            # increase the number of countries remaining
            self.num_of_countries = self.num_of_countries + 1

            # Adding the new territory on the list
            self.territory_list.append(self.revolution.new_territory)

            """
                Increasing the revolution possibility and decreasing the conquest possibility if possible
                (Conquest should always be available, that is why it should be over 0.001) by 0.001
            """
            if 0 <= self.revolution.probability <= 0.999 and 0.001 <= self.conquest.probability <= 1:
                self.revolution.increase_probability(0.001)
                self.conquest.decrease_probability(0.001)

        elif seed > self.revolution.probability:

            """
                A conquest will happen
            """

            # Portal Technology Activated!!!!!

            if seed <= self.revolution.probability + self.portal.probability:

                self.portal.run_portal(occupant)

                """
                    Examining whether the previous territory occupant has zero territories occupied
                    therefore they are defeated
                """
                if self.portal.opponent_is_defeated:

                    self.occupant_list.remove(self.portal.conquered.name)

                    self.num_of_countries -= 1

            elif seed > self.revolution.probability + self.portal.probability:

                """
                    A normal conquest will happen
                """

                self.conquest.run_conquest(occupant)

                """
                    Examining whether the previous territory occupant has zero territories occupied
                    therefore they are defeated
                """
                if self.conquest.opponent_is_defeated:

                    self.occupant_list.remove(self.conquest.conquered.name)

                    self.num_of_countries -= 1

            """
                Increasing the conquest possibility and decreasing the revolution possibility if possible
                (Conquest should always be available, that is why it should be over 0.001) by 0.001
            """
            if 0.002 <= self.revolution.probability <= 0.999 & 0.001 <= self.conquest.probability <= 0.998:
                self.revolution.increase_probability(0.002)
                self.conquest.decrease_probability(0.002)

        print(self.num_of_countries, "countries remaining.")

        self.portal.set_portal_probability(self.conquest.probability)
