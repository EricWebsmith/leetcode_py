import unittest


def combinations_with_replacement(n: int, k: int) -> int:
    ans = 1
    for i in range(1, k+1):
        ans *= (n + k - i)
        ans //= i
    return ans


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        return combinations_with_replacement(m, n-1)


def test(testObj: unittest.TestCase, m: int, n: int, expected: int) -> None:
    so = Solution()
    actual = so.uniquePaths(m, n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        print("test_1")
        test(self,   3,  7, 28)

    def test_2(self):
        print("test_2")
        test(self,   3,  2, 3)


if __name__ == '__main__':
    unittest.main()


'''
Beats 89.63%of users with Python3
'''
