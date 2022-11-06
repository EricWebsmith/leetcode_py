import unittest


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        start = n
        i = 0

        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            i += 1

        return n * (10 ** i) - start


def test(testObj: unittest.TestCase, n: int, target: int, expected: int) -> None:

    so = Solution()
    actual = so.makeIntegerBeautiful(n, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   16,  6, 4)

    def test_2(self):
        test(self,   467,  6, 33)

    def test_3(self):
        test(self,   1,  1, 0)

    def test_4(self):
        test(self,   19,  1, 81)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
55 ms
Beats
20%
'''
