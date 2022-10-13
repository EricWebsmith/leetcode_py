import unittest
from typing import Dict


class Solution:
    def isBalanced(self, d: Dict, avg: int):
        for v in d.values():
            if v > avg:
                return False

        return True

    def balancedString(self, s: str) -> int:
        n = len(s)
        avg = n // 4
        d = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for c in s:
            d[c] += 1

        if self.isBalanced(d, avg):
            return 0

        left = 0
        right = 0
        ans = n
        d[s[0]] -= 1
        while left <= right and right < n:
            if self.isBalanced(d, avg):
                ans = min(ans, right - left + 1)
                d[s[left]] += 1
                left += 1
            elif right < n-1:
                right += 1
                d[s[right]] -= 1
            else:
                break

        return ans


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:
    so = Solution()
    actual = so.balancedString(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "QWER", 0)

    def test_2(self):
        test(self,   "QQWE", 1)

    def test_3(self):
        test(self,   "QQQW", 2)

    def test_4(self):
        test(self,   "WWEQERQWQWWRWWERQWEQ", 4)


if __name__ == '__main__':
    unittest.main()

'''
409ms, 68.21%
'''
