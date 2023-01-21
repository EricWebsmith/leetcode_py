import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        counts = [0] * 26
        maxf = 0
        for right in range(n):
            right_index = ord(s[right]) - ord("A")
            counts[right_index] += 1
            maxf = max(maxf, counts[right_index])
            while (right - left + 1) - maxf > k:
                left_index = ord(s[left]) - ord("A")
                counts[left_index] -= 1
                left += 1

        return min(maxf + k, n)


def test(testObj: unittest.TestCase, s: str, k: int, expected: int) -> None:

    so = Solution()

    actual = so.characterReplacement(s, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "ABAB", 2, 4)

    def test_2(self):
        test(self, "AABABBA", 1, 4)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
111 ms
Beats
97.99%
"""
