import unittest
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        d = set()
        for _, v in c.items():
            if v in d:
                return False
            d.add(v)

        return True


def test(testObj: unittest.TestCase, arr: List[int], expected: bool) -> None:
    so = Solution()
    actual = so.uniqueOccurrences(arr)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 2, 1, 1, 3], True)

    def test_2(self):
        test(self,   [1, 2], False)

    def test_3(self):
        test(self,   [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True)

    def test_4(self):
        test(self,   [1, 2, 1, 2], False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
66 ms
Beats
59.77%
'''
