import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        str_list = [""] * numRows
        index = 0
        height = 0
        UP = -1
        DOWN = 1
        direction = DOWN

        while index < len(s):

            str_list[height] += s[index]

            # turn
            if direction == DOWN and height == numRows - 1:
                direction = UP

            if direction == UP and height == 0:
                direction = DOWN

            # step
            height = height + direction
            index += 1

        return "".join(str_list)


def test(testObj: unittest.TestCase, s: str, numRows: int, expected: str) -> None:
    so = Solution()
    actual = so.convert(s, numRows)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")

    def test_2(self):
        test(self, "PAYPALISHIRING", 4, "PINALSIGYAHRPI")

    def test_3(self):
        test(self, "A", 1, "A")


if __name__ == "__main__":
    unittest.main()


"""

"""
