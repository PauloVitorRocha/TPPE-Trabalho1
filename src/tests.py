import pytest
from activity_diagram import ActivityDiagram


def test_activity_diagram():
    obj = ActivityDiagram('ad1')
    assert 'ad1'==obj.name

def test_activity_diagram2():
    obj = ActivityDiagram('ad2')
    assert 'ad2'==obj.name
