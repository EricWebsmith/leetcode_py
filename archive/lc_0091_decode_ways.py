import unittest


class Solution:
    def one_step(self, s):
        return 0 if s == '0' else 1

    def two_steps(self, s):
        if s[0] == 0:
            return 0
        if s[0] == '1':
            return 1

        if s[0] == '2' and '0' <= s[1] <= '6':
            return 1

        return 0

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return self.one_step(s[0])
        a = 1
        b = self.one_step(s[0])
        c = a + b

        for i in range(1, n):
            c = a * self.two_steps(s[i-1:i+1]) + b * self.one_step(s[i])
            a = b
            b = c

        return c


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.numDecodings(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "12", 2)

    def test_2(self):
        test(self,   "226", 3)

    def test_3(self):
        test(self,   "06", 0)


if __name__ == '__main__':
    unittest.main()

'''
37ms, 87.73%
'''
