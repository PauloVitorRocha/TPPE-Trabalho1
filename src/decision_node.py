from transitions import ActivityTransitions


class DecisionStream():

    def __init__(self):
        self.transitions = []

        self.merge_node = None
        self.final_node = None

        self.activity_node = []

        self.elements = []

    def create_activity(self, activity_name):
        self.activity_node.append(activity_name)
        self.elements.append(0)

    def create_transition(self, transition_name, transition_prob):
        transition = ActivityTransitions(transition_name, transition_prob)
        self.transitions.append(transition)

    def create_merge(self, merge_name):
        self.merge_node = merge_name
        self.elements.append(2)

    def create_final(self, final_name):
        self.final_node = final_name
        self.elements.append(1)
