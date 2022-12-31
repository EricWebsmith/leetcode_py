import unittest


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(m):
            left = 0
            if m <= index + 1:
                left = (m + 1) * m >> 1
                left += index+1-m
            else:
                arr0 = m - index
                left = (m + arr0) * (index + 1) >> 1
            right = 0
            if m <= n-index:
                right = (m + 1) * m >> 1
                right += n - (index + m)
            else:
                arr_last = m - (n-index-1)
                right = (m + arr_last) * (n - index) >> 1
            return left + right - m

        left = 1
        right = maxSum - n + 1
        while left < right:
            m = (left + right + 1) >> 1
            s = get_sum(m)
            if s <= maxSum:
                left = m
            else:
                right = m - 1

        return left


def test(testObj: unittest.TestCase, n: int, index: int, maxSum: int, expected: int) -> None:
    so = Solution()
    actual = so.maxValue(n, index, maxSum)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,   4,  2,  6, 2)

    def test_2(self):
        test(self,   6,  1,  10, 3)


if __name__ == '__main__':
    unittest.main()


"""
Runtime
43 ms
Beats
83.70%
"""
