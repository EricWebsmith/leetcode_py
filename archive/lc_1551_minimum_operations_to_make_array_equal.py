import unittest


class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0

        if n == 2:
            return 1

        if n % 2 == 1:
            # arithmetic progression
            # we add (min + max) / 2 * n_nums
            # min_diff = 2
            # max_diff = (n - 1) // 2 * 2
            # return (min_diff + max_diff) // 2 * (n-1) // 2
            # return (n + 1) * (n-1) // 4 
            return (n * n - 1) >> 2
        else:
            # min_diff = 1
            # max_diff = n // 2 * 2 - 1
            # return (min_diff + max_diff) // 2 * n // 2
            return n * n >> 2
        

def test(testObj: unittest.TestCase, n: int, expected:int) -> None:
    so = Solution()
    actual = so.minOperations(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1, 0)

    def test_2(self):
        test(self,   2, 1)

    def test_3(self):
        test(self,   3, 2)

    def test_4(self):
        test(self,   4, 4)

    def test_5(self):
        test(self,   5, 6)

    def test_6(self):
        test(self,   6, 9)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
19 ms
Beats
99.42%
'''
