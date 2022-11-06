import unittest


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        ans = s
        if k == 1:
            for i in range(1, len(s)):
                t = s[i:] + s[:i]
                ans = min(ans, t)
        else:
            s = list(s)
            s.sort()
            ans = ''.join(s)
        return ans


def test(testObj: unittest.TestCase, s: str, k: int, expected: str) -> None:
    so = Solution()
    actual = so.orderlyQueue(s, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "cba",  1, "acb")

    def test_2(self):
        test(self,   "baaca",  3, "aaabc")


if __name__ == '__main__':
    unittest.main()

'''
Runtime
31 ms
Beats
97.62%
'''
