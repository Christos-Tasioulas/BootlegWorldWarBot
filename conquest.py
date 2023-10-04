from actions import Action
import random


class Conquest(Action):

    def __init__(self, probability):
        super().__init__('Conquest', probability)
        self.opponent_is_defeated = False
        self.conquered = None

    def run_conquest(self, occupant):

        # Selecting a random neighbor from the given country's neighbors

        random.seed(1)
        rand_int = random.randint(0, len(occupant.neighbors) - 1)
        territory = occupant.neighbors[rand_int]

        # changing the neighbor territory to occupied territory
        territory.set_prev_occupant()
        territory.set_occupant(occupant)
        occupant.add_territory(territory.name)
        occupant.remove_neighbor(territory.name)

        print(
            occupant.name +
            "has conquered" +
            territory.name +
            "previously occupied by" +
            territory.previous_occupant + "."
        )

        previous_occupant = territory.previous_occupant
        self.conquered = previous_occupant

        # remove the territory from the previous country's territories
        previous_occupant.remove_territory(territory.name)

        # adding new neighboring territories to the country
        for neighbor in previous_occupant.neighbors:

            if neighbor not in occupant.neighbors:
                occupant.add_neighbor(neighbor)

        """
            Examining whether the previous territory occupant has zero territories occupied
            therefore they are defeated
        """
        if len(previous_occupant.occupied_territories_names) == 0:

            for separatist_movement in previous_occupant.separatist_movements:

                # adding the previous occupant's separatist movements to this occupant
                if separatist_movement not in occupant.separatist_movements:
                    occupant.add_separatist_movement(separatist_movement)

            # add previous occupant to separatists movements
            occupant.add_separatist_movement(previous_occupant.name)
            defeated = previous_occupant.name
            print(defeated, "has been completely defeated")
            self.opponent_is_defeated = True
        else:
            self.opponent_is_defeated = False
