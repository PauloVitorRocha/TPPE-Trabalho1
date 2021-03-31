from activity_diagram import ActivityDiagram


def test_activity_diagram():
    obj = ActivityDiagram('ad1')
    assert 'ad1' == obj.name


def test_activity_diagram2():
    obj = ActivityDiagram('ad2')
    assert 'ad2' == obj.name


def test_activity_diagram3():
    obj = ActivityDiagram('ad3')
    assert 'ad3' == obj.name


def test_create_initial_node():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    assert 'n1' == obj.elements.start_node


def test_create_initial_node2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    assert 'n2' == obj.elements.start_node


def test_create_initial_node3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    assert 'n3' == obj.elements.start_node


def test_create_activity():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_activity('at1')
    assert 'at1' == obj.elements.activity_name[0]


def test_create_activity2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_activity('at2')
    assert 'at2' == obj.elements.activity_name[0]


def test_create_activity3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_activity('at3')
    assert 'at3' == obj.elements.activity_name[0]


def test_create_decision():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_decision('d1')
    assert 'd1' == obj.elements.decision_node[0]


def test_create_decision2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_decision('d2')
    assert 'd2' == obj.elements.decision_node[0]

def test_create_decision3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_decision('d3')
    assert 'd3'==obj.elements.decision_node[0]
