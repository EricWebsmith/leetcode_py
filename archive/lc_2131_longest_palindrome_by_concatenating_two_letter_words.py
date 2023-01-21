import unittest
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ALPHABETS = 26
        matrix = [[0] * ALPHABETS for _ in range(ALPHABETS)]
        for word in words:
            r = ord(word[0]) - ord("a")
            c = ord(word[1]) - ord("a")
            matrix[r][c] += 1

        answer = 0
        has_center = False
        for i in range(ALPHABETS):
            if matrix[i][i] % 2 == 0:
                answer += matrix[i][i]
            else:
                if not has_center:
                    answer += 1
                    has_center = True
                answer += matrix[i][i] - 1

        for r in range(ALPHABETS):
            for c in range(r + 1, ALPHABETS):
                answer += min(matrix[r][c], matrix[c][r]) * 2

        return answer * 2


def test(testObj: unittest.TestCase, words: List[str], expected: int) -> None:
    so = Solution()
    actual = so.longestPalindrome(words)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["lc", "cl", "gg"], 6)

    def test_2(self):
        test(self, ["ab", "ty", "yt", "lc", "cl", "ab"], 8)

    def test_3(self):
        test(self, ["cc", "ll", "xx"], 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1793 ms
Beats
78.93%

"""
