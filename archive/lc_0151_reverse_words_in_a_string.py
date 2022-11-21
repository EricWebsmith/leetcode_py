import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:
    so = Solution()
    actual = so.reverseWords(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "the sky is blue", "blue is sky the")

    def test_2(self):
        test(self,   "  hello world  ", "world hello")

    def test_3(self):
        test(self,   "a good   example", "example good a")


if __name__ == '__main__':
    unittest.main()

'''
Runtime
28 ms
Beats
98.47%
'''
