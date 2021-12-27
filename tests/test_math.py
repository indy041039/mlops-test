from mlspace.math import add_one, minus_one, double_it, half_it
import pytest


test_add_one_data = [
    (4,5),
    (5,6),
    (10,11)
]
@pytest.mark.parametrize('sample, expected_output', test_add_one_data)
def test_add_one(sample, expected_output):
    assert add_one(sample) == expected_output


def test_minus_one():
    assert minus_one(1)==0


def test_double_it():
    assert double_it(2)==4


def test_half_it():
    assert half_it(4)==2