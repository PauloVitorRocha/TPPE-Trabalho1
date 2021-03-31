import pytest
from activity_diagram import ActivityDiagram


def test_activity_diagram():
    obj = ActivityDiagram('ad1')
    assert 'ad1'==obj.name