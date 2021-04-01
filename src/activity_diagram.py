from elements import ActivityElements
from transitions import ActivityTransitions


class ActivityDiagram():

    def __init__(self, name):
        self.name = name
        self.transitions = []

    def create_initial_node(self, name):
        start_node = name
        self.elements = ActivityElements(start_node)

    def create_transitions(self, name, prob):
        transition = ActivityTransitions(name, prob)
        self.transitions.append(transition)
