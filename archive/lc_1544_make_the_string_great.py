import unittest


class Solution:
    def makeGood(self, s: str) -> str:
        stack: list = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == ord("a") - ord("A"):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:
    so = Solution()
    actual = so.makeGood(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "leEeetcode", "leetcode")

    def test_2(self):
        test(self, "abBAcC", "")

    def test_3(self):
        test(self, "s", "s")


if __name__ == "__main__":
    unittest.main()

"""
Runtime
42 ms
Beats
88.98%
"""
