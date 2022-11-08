import unittest


class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s)-1:
            if abs(ord(s[i]) - ord(s[i+1])) == ord('a') - ord('A'):
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1

        return s


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:

    so = Solution()
    actual = so.makeGood(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "leEeetcode", "leetcode")

    def test_2(self):
        test(self,   "abBAcC", "")

    def test_3(self):
        test(self,   "s", "s")


if __name__ == '__main__':
    unittest.main()

'''

'''
