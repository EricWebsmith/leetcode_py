import unittest


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(n: int, k: int) -> int:
            if n == 0:
                return 0
            p = rec(n-1, k//2)
            if k % 2 == 0:
                return p
            else:
                return 1-p

        return rec(n, k-1)


def test(testObj: unittest.TestCase, n: int, k: int, expected: int) -> None:
    so = Solution()
    actual = so.kthGrammar(n, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1,  1, 0)

    def test_2(self):
        test(self,   2,  1, 0)

    def test_3(self):
        test(self,   2,  2, 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
27 ms
Beats
98.16%
'''
