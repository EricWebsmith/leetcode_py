import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        post_max = [0] * n
        moving_max = events[-1][2]
        for i in range(n-1, -1, -1):
            moving_max = max(moving_max, events[i][2])
            post_max[i] = moving_max

        cache = {}

        def dfs(index, left_k):
            if (index, left_k) in cache:
                return cache[(index, left_k)]
            if index == n - 1:
                return events[-1][2]

            if left_k == 1:
                return post_max[index]
            # select this
            _, end_day, value = events[index]

            # binary search to find next index
            left = index + 1
            right = n
            while left < right:
                mid = (left + right) >> 1
                if events[mid][0] <= end_day:
                    left = mid + 1
                else:
                    right = mid

            next_index = left

            select_this = value
            # no more available, return this value
            if next_index < n:
                select_this = value + dfs(next_index, left_k-1)

            not_select_this = dfs(index + 1, left_k)
            ans = max(select_this, not_select_this)
            cache[(index, left_k)] = ans
            return ans

        ans = dfs(0, k)
        return ans


def test(testObj: unittest.TestCase, events: List[List[int]], k: int, expected: int) -> None:

    so = Solution()
    actual = so.maxValue(events, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 2, 4], [3, 4, 3], [2, 3, 1]],  2, 7)

    def test_2(self):
        test(self,   [[1, 2, 4], [3, 4, 3], [2, 3, 10]],  2, 10)

    def test_3(self):
        test(self,   [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]],  3, 9)

    def test_4(self):
        test(self,   [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]],  2, 7)

    def test_5(self):
        test(self,   [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]],  100, 10)

    def test_6(self):
        test(self,  [[1, 3, 4], [2, 4, 1], [
             1, 1, 4], [3, 5, 1], [2, 5, 5]], 3, 9)

    def test_7(self):
        test(self,  [[2, 4, 1], [1, 1, 4], [2, 5, 5]], 3, 9)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 942 ms, faster than 95.36% of Python3 online submissions for Maximum Number of Events That Can Be Attended II.
Memory Usage: 61 MB, less than 63.29% of Python3 online submissions for Maximum Number of Events That Can Be Attended II.
'''
