import unittest


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        move = 0
        s = 0
        for i in range(1, n+1):
            while i >> move > 0:
                move += 1
            s <<= move
            s += i
            s %= MOD

        return s


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()

    actual = so.concatenatedBinary(n)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1, 1)

    def test_2(self):
        test(self,   2, 6)

    def test_3(self):
        test(self,   3, 27)

    def test_4(self):
        test(self,   4, 220)

    def test_5(self):
        test(self,   5, 1765)

    def test_12(self):
        test(self,   12, 505379714)

    def test_100(self):
        test(self,   100, 310828084)

    def test_10000(self):
        test(self,   10000, 356435599)

    def test_100000(self):
        test(self, 100000, 757631812)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1183 ms, faster than 96.06%
Memory Usage: 13.8 MB, less than 80.31%
'''
