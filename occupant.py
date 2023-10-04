"""
    Describes each country remaining in the war 
"""

import color


class Occupant:
    """
        This class includes:
        -(str) name, the primary key
        -(list of strings) occupied_territories_names, a list with all the names of territories the country 
        occupies
        -(list of strings) separatist_movements, a list with all the names of the separatist movements of the occupant
        -(list of strings) neighbors, a list with all the names of the neighboring countries
        -(class color) color, distinct for every occupant
    """

    def __init__(self, name, separatist_movements, neighbors):
        self.name = name
        self.occupied_territories_names = [name]
        self.separatist_movements = separatist_movements
        self.neighbors = neighbors
        self.color = color.Color(255)

    def add_territory(self, territory):
        self.occupied_territories_names.append(territory)

    def remove_territory(self, territory):
        self.occupied_territories_names = [x for x in self.occupied_territories_names if x != territory]

    def add_separatist_movement(self, separatist_movement):
        self.separatist_movements.append(separatist_movement)

    def remove_separatist_movement(self, separatist_movement):
        self.separatist_movements = [x for x in self.separatist_movements if x != separatist_movement]

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        self.neighbors = [x for x in self.neighbors if x != neighbor]
