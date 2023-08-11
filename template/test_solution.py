import pytest

from solution import Solution


@pytest.mark.parametrize(
    "inputs,expected",
    [
        # enter test inputs here
    ],
)
def test(benchmark, inputs, expected):
    assert expected == benchmark(
        # solution function here
    )
