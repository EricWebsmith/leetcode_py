import unittest
from typing import List, Optional, Dict, Set, Any
null = None


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m):
            for c in range(n):
                dp[r+1][c+1] = dp[r][c+1] + dp[r+1][c] - \
                    dp[r][c] + matrix[r][c]

        ans = 0
        for r in range(m):
            for c in range(n):
                max_w = min(m-r, n-c)
                for w in range(1, max_w+1):
                    s = dp[r+w][c+w] - dp[r+w][c] - dp[r][c+w] + dp[r][c]
                    if s == w * w:
                        ans += 1
                    else:
                        break

        return ans


def test(testObj: unittest.TestCase, matrix: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.countSquares(matrix)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, [[0, 1, 1, 1],  [1, 1, 1, 1],  [0, 1, 1, 1], ], 15)

    def test_2(self):
        test(self, [[1, 0, 1], [1, 1, 0],  [1, 1, 0], ], 7)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 940 ms, faster than 63.89% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 18.4 MB, less than 6.48% of Python3 online submissions for Count Square Submatrices with All Ones.
'''
