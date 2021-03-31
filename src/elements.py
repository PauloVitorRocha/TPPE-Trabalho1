class ActivityElements():

    def __init__(self, start_node):
        self.start_node = start_node
        self.activity_name = []
        self.elements_order = []

    def create_activity(self, name):
        activity = name
        self.activity_name.append(activity)
        self.elements_order.append(0)
