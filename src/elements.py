class ActivityElements():

    def __init__(self, start_node):
        self.start_node = start_node

        self.activity_name = []
        self.elements_order = []
        self.decision_node = []

    def create_activity(self, name):
        activity = name
        self.activity_name.append(activity)

        self.elements_order.append(0)

    def create_decision(self, name):
        decision = 'd1'
        self.decision_node.append(decision)

        self.elements_order.append(1)
