import unittest
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        open_count = 0
        close_count = 0
        close_errs: list = []
        for i in range(n):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                close_count += 1
            if close_count > open_count:
                close_errs.append(i)
                close_count -= 1

        open_count = 0
        close_count = 0
        open_errs: list = []
        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                close_count += 1
            if open_count > close_count:
                open_errs.append(i)
                open_count -= 1

        if not open_errs and not close_errs:
            return [s]

        left = "" if len(close_errs) == 0 else s[: close_errs[-1] + 1]
        middle = ""
        right = s
        if open_errs and close_errs:
            middle = s[close_errs[-1] + 1 : open_errs[-1]]
        elif close_errs:
            middle = s[close_errs[-1] + 1 :]
        elif open_errs:
            middle = s[: open_errs[-1]]

        correct_left = set()

        def dfs_left(s_left, err_index):
            if err_index == len(close_errs):
                s_left = s_left.replace(" ", "")
                correct_left.add(s_left)
                return
            err_at = close_errs[err_index]
            for i in range(err_at + 1):
                if s_left[i] == ")":
                    new_s_left = s_left[:i] + " " + s_left[i + 1 :]
                    dfs_left(new_s_left, err_index + 1)

        dfs_left(left, 0)

        correct_right = set()

        def dfs_right(s_right, err_index):
            if err_index == len(open_errs):

                if open_errs:
                    s_right = s_right[open_errs[-1] :]
                else:
                    s_right = ""
                s_right = s_right.replace(" ", "")
                correct_right.add(s_right)
                return
            err_at = open_errs[err_index]
            for i in range(err_at, n):
                if s_right[i] == "(":
                    new_s_right = s_right[:i] + " " + s_right[i + 1 :]
                    dfs_right(new_s_right, err_index + 1)

        dfs_right(right, 0)

        ans: list = []
        for s_left in correct_left:

            for s_right in correct_right:
                ans.append(s_left + middle + s_right)
        return ans


def test(testObj: unittest.TestCase, s: str, expected: List[str]) -> None:

    so = Solution()

    actual = so.removeInvalidParentheses(s)
    actual.sort()
    expected.sort()

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "()())()", ["(())()", "()()()"])

    def test_2(self):
        test(self, "(a)())()", ["(a())()", "(a)()()"])

    def test_3(self):
        test(self, ")(", [""])

    def test_4(self):
        test(self, ")((((((", [""])

    def test_5(self):
        test(self, ")()", ["()"])

    def test_6(self):
        test(self, ")", [""])

    def test_7(self):
        test(self, "(", [""])

    def test_8(self):
        test(self, "()", ["()"])

    def test_9(self):
        test(self, "n", ["n"])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 113 ms, faster than 81.63%
Memory Usage: 13.9 MB, less than 82.96%
"""
