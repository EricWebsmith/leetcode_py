import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children: List[Node] = children if children is not None else []

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        node_dict = {}
        kill_node: Node = None
        for id in pid:
            node = Node(id)
            node.children = []
            node_dict[id] = node
            if id == kill:
                kill_node = node

        for child_id, parent_id in zip(pid, ppid):
            child_node: Node = node_dict[child_id]
            if parent_id == 0:
                continue
            parent_node: Node = node_dict[parent_id]
            parent_node.children.append(child_node)

        ans = []

        def dfs(node: Node):
            ans.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(kill_node)
        return ans


def test(testObj: unittest.TestCase, pid: List[int], ppid: List[int], kill: int, expected: List[int]) -> None:

    so = Solution()

    actual = so.killProcess(pid, ppid, kill)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 10, 5],  [3, 0, 5, 3],  5, [5, 10])

    def test_2(self):
        test(self,   [1],  [0],  1, [1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 545 ms, faster than 75.99%
Memory Usage: 31 MB, less than 7.92%
'''
