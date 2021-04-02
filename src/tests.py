from activity_diagram import ActivityDiagram
from decision_node import DecisionStream

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


def test_initiate_decision():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.initiate_decision(1)
    assert [[]] == obj.elements.decision_node


def test_initiate_decision2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.initiate_decision(2)
    assert [[], []] == obj.elements.decision_node


def test_initiate_decision3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.initiate_decision(3)
    assert [[], [], []] == obj.elements.decision_node


def test_init_decision():
    decision = DecisionStream()
    assert [] == decision.transitions
    assert None == decision.merge_node
    assert None == decision.final_node
    assert [] == decision.activity_node
    assert [] == decision.elements


def test_init_decision2():
    decision = DecisionStream()
    assert [] == decision.transitions
    assert None == decision.merge_node
    assert None == decision.final_node
    assert [] == decision.activity_node
    assert [] == decision.elements


def test_init_decision3():
    decision = DecisionStream()
    assert [] == decision.transitions
    assert None == decision.merge_node
    assert None == decision.final_node
    assert [] == decision.activity_node
    assert [] == decision.elements

def test_decision_create_activity():
    decision = DecisionStream()
    decision.create_activity("nda1")
    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda1"

def test_decision_create_activity2():
    decision = DecisionStream()
    decision.create_activity("nda2")
    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda2"

def test_decision_create_activity3():
    decision = DecisionStream()
    decision.create_activity("nda3")
    decision.create_activity("nda3.1")
    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda3"
    assert decision.elements[1] == 0
    assert decision.activity_node[1] == "nda3.1"

def test_decision_create_transition():
    decision = DecisionStream()
    decision.create_transition("ndt1", 19.49)
    assert decision.transitions[0].transition_name == "ndt1"
    assert decision.transitions[0].transition_prob == 19.49

def test_decision_create_transition2():
    decision = DecisionStream()
    decision.create_transition("ndt2", 19.50)
    assert decision.transitions[0].transition_name == "ndt2"
    assert decision.transitions[0].transition_prob == 19.50

def test_decision_create_transition3():
    decision = DecisionStream()
    decision.create_transition("ndt3", 19.51)
    decision.create_transition("ndt3.1", 19.52)
    assert decision.transitions[0].transition_name == "ndt3"
    assert decision.transitions[0].transition_prob == 19.51
    assert decision.transitions[1].transition_name == "ndt3.1"
    assert decision.transitions[1].transition_prob == 19.52

def test_decision_create_merge():
    decision = DecisionStream()
    decision.create_merge("ndm1")
    assert decision.elements[0] == 2
    assert decision.merge_node == "ndm1"

def test_decision_create_merge2():
    decision = DecisionStream()
    decision.create_merge("ndm2")
    assert decision.elements[0] == 2
    assert decision.merge_node == "ndm2"

def test_decision_create_merge3():
    decision = DecisionStream()
    decision.create_merge("ndm3") 
    assert decision.elements[0] == 2
    assert decision.merge_node == "ndm3"

def test_decision_create_final():
    decision = DecisionStream()
    decision.create_final("ndf1")
    assert decision.elements[0] == 1
    assert decision.final_node == "ndf1"

def test_decision_create_final2():
    decision = DecisionStream()
    decision.create_final("ndf2")
    assert decision.elements[0] == 1
    assert decision.final_node == "ndf2"

def test_decision_create_final3():
    decision = DecisionStream()
    decision.create_final("ndf3") 
    assert decision.elements[0] == 1
    assert decision.final_node == "ndf3"

def test_create_decision():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.initiate_decision(1)
    decision = DecisionStream()

    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_decision('d1')
    assert 'd1' == obj.elements.decision_node[0]


# def test_create_decision2():
#     obj = ActivityDiagram('ad2')
#     obj.create_initial_node('n2')
#     obj.elements.create_decision('d2')
#     assert 'd2' == obj.elements.decision_node[0]


# def test_create_decision3():
#     obj = ActivityDiagram('ad3')
#     obj.create_initial_node('n3')
#     obj.elements.create_decision('d3')
#     assert 'd3' == obj.elements.decision_node[0]


def test_create_merge():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_merge('m1')
    assert 'm1' == obj.elements.merge_node[0]


def test_create_merge2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_merge('m2')
    assert 'm2' == obj.elements.merge_node[0]


def test_create_merge3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_merge('m3')
    assert 'm3' == obj.elements.merge_node[0]


def test_create_final():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_final('f1')
    assert 'f1' == obj.elements.final_node[0]


def test_create_final2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_final('f2')
    assert 'f2' == obj.elements.final_node[0]


def test_create_final3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_final('f3')
    assert 'f3' == obj.elements.final_node[0]


def test_create_transition():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.create_transitions('t1', 0.01)
    assert 't1' == obj.transitions[0].transition_name
    assert 0.01 == obj.transitions[0].transition_prob


def test_create_transition2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.create_transitions('t2', 0.09)
    assert 't2' == obj.transitions[0].transition_name
    assert 0.09 == obj.transitions[0].transition_prob


def test_create_transition3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.create_transitions('t3', 0.90)
    assert 't3' == obj.transitions[0].transition_name
    assert 0.90 == obj.transitions[0].transition_prob
