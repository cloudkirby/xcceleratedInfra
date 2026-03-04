import pytest
from ..transform.transform import print_hi

def test_main():
    assert print_hi('World') == 'Hi, World'