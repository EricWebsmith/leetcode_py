import unittest


class Solution:
    def __init__(self) -> None:
        self.s = ''
        self.dp: list = []

    def minCut(self, s: str) -> int:
        n = len(s)

        self.s = s
        self.dp = [i for i in range(n)]
        for i in range(n):
            self.findMinimumCuts(i, i)
            self.findMinimumCuts(i, i+1)

        return self.dp[-1]

    def findMinimumCuts(self, start_index: int, end_index: int):
        """
        Expand Around the Center
        """
        s = self.s
        n = len(s)
        dp = self.dp
        start = start_index
        end = end_index
        while start >= 0 and end < n and s[start] == s[end]:
            new_cut = 0
            if start > 0:
                new_cut = dp[start-1] + 1
            dp[end] = min(dp[end], new_cut)
            start -= 1
            end += 1


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:
    so = Solution()
    actual = so.minCut(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "aab", 1)

    def test_2(self):
        test(self,   "a", 0)

    def test_3(self):
        test(self,   "ab", 1)

    def test_4(self):
        test(self,   "aaba", 1)

    def test_5(self):
        test(self,   "baab", 0)

    def test_6(self):
        test(self,   "cbaab", 1)

    def test_7(self):
        test(self,   "cabababcbc", 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 775 ms, faster than 83.38%
Memory Usage: 13.9 MB, less than 88.54%
'''
