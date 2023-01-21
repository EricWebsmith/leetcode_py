import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(t[::-1] for t in s.split(" "))


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:

    so = Solution()

    actual = so.reverseWords(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")

    def test_2(self):
        test(self, "God Ding", "doG gniD")


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 53 ms, faster than 73.28%
Memory Usage: 14.6 MB, less than 46.10%
"""
