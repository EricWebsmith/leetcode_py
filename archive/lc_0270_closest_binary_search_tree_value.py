import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best_val = -1
        best_dis = 1_000_000

        current = root
        while current:
            dis = current.val - target
            abs_dis = abs(current.val - target)
            if abs_dis < best_dis:
                best_dis = abs_dis
                best_val = current.val

            if dis > 0:
                current = current.left
            else:
                current = current.right

        return best_val


def test(testObj: unittest.TestCase, root_arr: List[int|None], target: float, expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()

    actual = so.closestValue(root, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [4, 2, 5, 1, 3], 3.714286, 4)

    def test_2(self):
        test(self, [1], 4.428571, 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 57 ms, faster than 65.16%
Memory Usage: 16.2 MB, less than 34.57%
"""
