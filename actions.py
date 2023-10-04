"""
    This module describes the actions that are possible to happen during the war
    Note: the possibilities of each action would change depending on their frequency during the run
"""
from abc import ABC, abstractmethod


class Action(ABC):
    """
        includes: 
        -(string) name, the name of action, that is to say the action, can either be a conquest or a revolution
        -(float) probability, how possible the action is to happen during the run
    """

    def __init__(self, name, probability):

        self.name = name
        self.probability = probability

    """
        Change could be a string having as value either "Increase" or "Decrease"
        the num is the number added or subtracted from the previous probability value,
        should be less than 1
    """

    def increase_probability(self, num):
        # Increasing the probability of the action by num
        self.probability = self.probability + num

    def decrease_probability(self, num):
        # Decreasing the probability of the action by num
        self.probability = self.probability - num
