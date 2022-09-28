import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)

        ans = 0
        for k, v in d.items():
            if v < 2:
                return -1
            ans += v // 3
            if v % 3 > 0:
                ans += 1
        return ans


def test(testObj: unittest.TestCase, tasks: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minimumRounds(tasks)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4)

    def test_2(self):
        test(self,   [2, 3, 3], -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 932 ms, faster than 99.47% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
Memory Usage: 28.5 MB, less than 38.92% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
'''
