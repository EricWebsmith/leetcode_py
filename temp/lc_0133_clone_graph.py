import unittest
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: List['Node'] = neighbors if neighbors is not None else [
        ]


class Solution:
    def __init__(self) -> None:
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        if node.val in self.visited:
            return self.visited[node.val]

        cloned = Node(node.val, [])
        self.visited[node.val] = cloned

        cloned.neighbors = [self.cloneGraph(
            neighbor) for neighbor in node.neighbors]

        return cloned


def test(testObj: unittest.TestCase, node_arr: List[int], expected: 'Node') -> None:
    # node = array_to_node(node_arr)
    # so = Solution()

    # actual = so.cloneGraph(node)

    # testObj.assertEqual(actual, expected)
    pass


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[2, 4], [1, 3], [2, 4], [1, 3]],
             [[2, 4], [1, 3], [2, 4], [1, 3]])

    def test_2(self):
        test(self,   [[]], [[]])

    def test_3(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
42 ms
Beats
90.97%
'''
