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
    assert 'n1'==obj.elements.start_node