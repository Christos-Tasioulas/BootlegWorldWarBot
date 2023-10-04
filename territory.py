import occupant


class Territory:
    """
    Class Territory includes:
    - (string) name, the primary key of the territory
    - (class occupant) occupant
    - (class occupant) previous_occupant, mainly for display reasons and determining this occupant's fate easier
    """

    def __init__(self, name, separatist_movements, neighbor_list):
        self.name = name
        self.occupant = occupant.Occupant(name, separatist_movements, neighbor_list)
        self.previous_occupant = self.occupant
        self.color = self.occupant.color

    def set_occupant(self, new_occupant):
        self.occupant = new_occupant

    def set_prev_occupant(self):
        self.previous_occupant = self.occupant

    def set_color(self):
        self.color = self.occupant.color
