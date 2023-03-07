import unittest


class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        return 1 + n * (n - 1) * 2


def test(testObj: unittest.TestCase, n: int, expected:int) -> None:
    so = Solution()
    actual = so.coloredCells(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1, 1)

    def test_2(self):
        test(self,   2, 5)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
23 ms
Beats
100%
'''
