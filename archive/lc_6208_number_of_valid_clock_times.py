import unittest


class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(":")
        n_hours = 1
        if hh == "??":
            n_hours = 24
        elif hh[0] == "?":
            if hh[1] <= "3":
                n_hours = 3
            else:
                n_hours = 2
        elif hh[1] == "?":
            if hh[0] == "2":
                n_hours = 4
            else:
                n_hours = 10

        n_minutes = 1
        if mm[0] == "?":
            n_minutes *= 6
        if mm[1] == "?":
            n_minutes *= 10

        return n_hours * n_minutes


def test(testObj: unittest.TestCase, time: str, expected: int) -> None:

    so = Solution()

    actual = so.countTime(time)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "?5:00", 2)

    def test_2(self):
        test(self, "0?:0?", 100)

    def test_3(self):
        test(self, "??:??", 1440)

    def test_4(self):
        test(self, "2?:??", 240)


if __name__ == "__main__":
    unittest.main()

"""

"""
