import unittest


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = (n - 1) * 2
        time = time % mod
        if time <= n - 1:
            return time + 1
        else:
            return n * 2 - time - 1


def test(testObj: unittest.TestCase, n: int, time: int, expected: int) -> None:
    so = Solution()
    actual = so.passThePillow(n, time)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   4,  5, 2)

    def test_2(self):
        test(self,   3,  2, 3)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
21 ms
Beats
98.55%
'''
