import unittest
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], num: int) -> int:
        n_digits = len(digits)
        s = str(num)
        n = len(s)
        ans = sum(n_digits ** i for i in range(1, n))
        for i, c in enumerate(s):
            ans += n_digits ** (n-i-1) * sum(d < c for d in digits)
            if c not in digits:
                return ans

        return ans + 1


def test(testObj: unittest.TestCase, digits: List[str], n: int, expected: int) -> None:
    so = Solution()
    actual = so.atMostNGivenDigitSet(digits, n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["1", "3", "5", "7"],  100, 20)

    def test_2(self):
        test(self,   ["1", "4", "9"],  1000000000, 29523)

    def test_3(self):
        test(self,   ["7"],  8, 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
37 ms
Beats
83.71%
'''
