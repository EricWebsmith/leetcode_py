import unittest


class Solution:
    def countDigits(self, num: int) -> int:
        t = num
        ans = 0
        while t:
            d = t % 10
            if num % d == 0:
                ans += 1
            t = t // 10

        return ans


def test(testObj: unittest.TestCase, num: int, expected: int) -> None:
    so = Solution()
    actual = so.countDigits(num)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   7, 1)

    def test_2(self):
        test(self,   121, 2)

    def test_3(self):
        test(self,   1248, 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
32 ms
Beats
100%
'''
