import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        num_index_dict = {num: i for i, num in enumerate(target)}
        arr_indices = []
        for num in arr:
            if num in num_index_dict:
                arr_indices.append(num_index_dict[num])

        if len(arr_indices) == 0:
            return len(target)

        increase_arr = [arr_indices[0]]
        for i in arr_indices[1:]:
            if i > increase_arr[-1]:
                increase_arr.append(i)
            else:
                index = bisect_left(increase_arr, i)
                increase_arr[index] = i

        return len(target) - len(increase_arr)


def test(testObj: unittest.TestCase, target: List[int], arr: List[int], expected: int) -> None:

    so = Solution()

    actual = so.minOperations(target, arr)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [5, 1, 3],  [9, 4, 2, 3, 4], 2)

    def test_2(self):
        test(self,   [6, 4, 8, 1, 3, 2],  [4, 7, 6, 2, 3, 8, 6, 1], 3)

    def test_3(self):
        test(self,   [6],  [4, 7, 6, 2, 3, 8, 6, 1], 0)

    def test_4(self):
        test(self,   [1, 2, 3, 4],  [4, 3, 2, 1], 3)

    def test_5(self):
        test(self,   [1, 2, 3, 4],  [1, 4, 3, 2, 1], 2)

    def test_6(self):
        test(self,   [1, 3, 8], [2, 6], 3)

    def test_7(self):
        test(self,   [1, 3, 8], [2, 6, 8], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1005 ms, faster than 96.15%
Memory Usage: 36.9 MB, less than 91.03%
'''
