from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort()
        post_max_defence = [0] * n
        post_max_defence[n-1] = properties[n-1][1]
        for i in range(n-2, -1, -1):
            print(i)
            post_max_defence[i] = max(post_max_defence[i+1], properties[i][1])

        next_attack_at = {}
        for i in range(1, n):
            if properties[i-1][0] < properties[i][0]:
                next_attack_at[properties[i-1][0]] = i

        ans = 0
        for i in range(n):
            # max attack
            if not properties[i][0] in next_attack_at:
                break

            next_attack_index = next_attack_at[properties[i][0]]
            next_max_defence = post_max_defence[next_attack_index]
            if properties[i][1] < next_max_defence:
                ans += 1

        return ans


def test(testObj: unittest.TestCase, properties: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.numberOfWeakCharacters(properties)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[5, 5], [6, 3], [3, 6]], 0)

    def test_2(self):
        test(self,   [[2, 2], [3, 3]], 1)

    def test_3(self):
        test(self,   [[1, 5], [10, 4], [4, 3]], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 2619 ms, faster than 83.36% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 70.4 MB, less than 10.18% of Python3 online submissions for The Number of Weak Characters in the Game.
'''
