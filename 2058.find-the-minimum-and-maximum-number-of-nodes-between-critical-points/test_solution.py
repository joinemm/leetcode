import pytest

from solution import ListNode, Solution


def get_head(inputs):
    prev_node = None
    head = None
    for i in range(len(inputs)):
        node = ListNode(val=inputs[i])
        if i == 0:
            head = node
        if prev_node:
            prev_node.next = node
        prev_node = node

    return head


@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([1, 3], [-1, -1]),
        ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
        ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ],
)
def test(benchmark, inputs, expected):
    assert expected == benchmark(
        Solution().nodesBetweenCriticalPoints, get_head(inputs)
    )
