import unittest


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        bulky = (
            length >= 10_000
            or width >= 10_000
            or height >= 10_000
            or mass >= 10_000
            or length * width * height >= 1_000_000_000
        )
        heavy = mass >= 100
        both = bulky and heavy
        neither = not bulky and not heavy

        if both:
            return "Both"
        elif neither:
            return "Neither"
        elif bulky:
            return "Bulky"
        else:
            return "Heavy"


def test(
    testObj: unittest.TestCase,
    length: int,
    width: int,
    height: int,
    mass: int,
    expected: str,
) -> None:
    so = Solution()
    actual = so.categorizeBox(length, width, height, mass)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 1000, 35, 700, 300, "Heavy")

    def test_2(self):
        test(self, 200, 50, 800, 50, "Neither")

    def test_3(self):
        test(self, 2909, 3968, 3272, 727, "Both")


if __name__ == "__main__":
    unittest.main()

"""
Runtime
29 ms
Beats
79.20%
"""
