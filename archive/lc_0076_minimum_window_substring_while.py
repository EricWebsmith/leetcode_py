import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        bag = [0] * 128
        for c in t:
            bag[ord(c)] += 1

        n = len(s)
        left = 0
        best = ""
        best_length = 1000000000
        counter = len(t)

        for right in range(n):
            right_index = ord(s[right])
            if bag[right_index] > 0:
                counter -= 1
            bag[right_index] -= 1
            while counter == 0:
                left_index = ord(s[left])
                bag[left_index] += 1
                if bag[left_index] > 0:
                    counter += 1
                    length = right - left + 1
                    if length < best_length:
                        best_length = length
                        best = s[left: right + 1]
                left += 1
        return best


def test(testObj: unittest.TestCase, s: str, t: str, expected: str) -> None:

    so = Solution()
    actual = so.minWindow(s, t)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "ADOBECODEBANC", "ABC", "BANC")

    def test_2(self):
        test(self, "a", "a", "a")

    def test_3(self):
        test(self, "a", "aa", "")

    def test_4(self):
        test(self, "ab", "A", "")


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1930 ms
Beats
5%
"""
