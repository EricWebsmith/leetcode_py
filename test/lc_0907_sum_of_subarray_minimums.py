import unittest
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        s = 0
        stack = []

        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid-left) * (right-mid)
                s += count * arr[mid]

            stack.append(i)

        return s % MOD


def test(testObj: unittest.TestCase, arr: List[int], expected: int) -> None:
    so = Solution()
    actual = so.sumSubarrayMins(arr)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 1, 2, 4], 17)

    def test_2(self):
        test(self,   [11, 81, 94, 43, 3], 444)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
480 ms
Beats
93.14%
'''
