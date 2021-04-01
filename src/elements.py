class ActivityElements():

    def __init__(self, start_node):
        self.start_node = start_node

        self.activity_name = []
        self.elements_order = []
        self.decision_node = []
        self.merge_node = []
        self.final_node = []

    def create_activity(self, name):
        activity = name
        self.activity_name.append(activity)

        self.elements_order.append(0)

    def create_decision(self, name):
        decision = name
        self.decision_node.append(decision)

        self.elements_order.append(1)

    def create_merge(self, name):
        merge = name
        self.merge_node.append(merge)

        self.elements_order.append(2)

    def create_final(self, name):
        final = name
        self.final_node.append(final)

        self.elements_order.append(3)
