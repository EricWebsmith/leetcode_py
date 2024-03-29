import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        s = list(s)  # type: ignore
        index = n - 1
        start_removing = False
        end = -1
        stars = 0
        while index >= 0:
            if s[index] == "*":
                start_removing = True
                if end == -1:
                    end = index
                stars += 1
            elif start_removing:
                stars -= 1

            if start_removing and stars == 0 and (index > 0 and s[index - 1] != "*" or index == 0):
                t: list = []
                if index > 0:
                    t += s[:index]
                if end < n - 1:
                    t += s[end + 1:]
                s = t  # type: ignore
                start_removing = False
                stars = 0
                end = -1

            index -= 1
        return "".join(s)


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.removeStars(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "leet**cod*e", "lecoe")

    def test_2(self):
        test(self, "erase*****", "")


if __name__ == "__main__":
    unittest.main()

"""

"""
