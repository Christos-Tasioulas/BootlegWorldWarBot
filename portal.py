from actions import Action
import random


class Portal(Action):

    def __init__(self, probability, territory_list):
        super().__init__('Portal', probability)
        self.territory_list = territory_list
        self.opponent_is_defeated = False
        self.conquered = None

    """
        Portal conquests will always be 80 times less likely than normal conquests
    """
    def set_portal_probability(self, conquest_probability):
        self.probability = conquest_probability / 80

    def run_portal(self, occupant):

        # Selecting a random territory for the occupant to portal to
        random.seed(1)
        rand_int = random.randint(0, len(self.territory_list))
        territory = self.territory_list[rand_int]

        # changing the neighbor territory to occupied territory
        territory.set_prev_occupant()
        territory.set_occupant(occupant)
        occupant.add_territory(territory.name)

        print(
            occupant.name +
            "has conquered" +
            territory.name +
            "previously occupied by" +
            territory.previous_occupant +
            "using portal technology."
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
