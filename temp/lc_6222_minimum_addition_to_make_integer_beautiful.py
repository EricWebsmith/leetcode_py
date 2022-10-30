import unittest


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        parts = []
        while n:
            i = n % 10
            n = n // 10
            parts.append(i)

        ans = 0
        parts.reverse()
        for p in parts:
            if target > p:
                target -= p
            elif target == p:
                target = 0
            else:
                ans = ans * 10 + (9-p)

        if ans > 0:
            ans += 1
        return ans


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

'''
