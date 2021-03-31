from elements import ActivityElements


class ActivityDiagram():

    def __init__(self, name):
        self.name = name

    def create_initial_node(self, name):
        start_node = name
        self.elements = ActivityElements(start_node)
