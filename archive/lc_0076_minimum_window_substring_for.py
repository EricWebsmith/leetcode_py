import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = [0] * 128
        for c in t:
            need[ord(c)] += 1
        need_all = len(t)

        n = len(s)
        left = 0
        best = ''
        best_length = 1000000000

        for right in range(n):
            right_index = ord(s[right])
            if need[right_index] > 0:
                need_all -= 1
            need[right_index] -= 1
            while need_all == 0:
                left_index = ord(s[left])
                need[left_index] += 1
                if need[left_index] > 0:
                    need_all += 1
                    length = right - left + 1
                    if length < best_length:
                        best_length = length
                        best = s[left: right+1]
                left += 1

        return best


def test(testObj: unittest.TestCase, s: str, t: str, expected: str) -> None:

    so = Solution()
    actual = so.minWindow(s, t)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "ADOBECODEBANC",  "ABC", "BANC")

    def test_2(self):
        test(self,   "a",  "a", "a")

    def test_3(self):
        test(self,   "a",  "aa", "")

    def test_4(self):
        test(self,   "ab",  "A", "")


if __name__ == '__main__':
    unittest.main()

'''
Runtime
230 ms
Beats
51.67%
'''
