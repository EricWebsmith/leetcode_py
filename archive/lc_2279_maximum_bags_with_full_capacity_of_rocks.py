import unittest


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        spaces: list[int] = [c - r for c, r in zip(capacity, rocks)]
        spaces.sort()
        ans = 0
        for space in spaces:
            if additionalRocks >= space:
                additionalRocks -= space
                ans += 1
            else:
                break

        return ans


def test(
    testObj: unittest.TestCase,
    capacity: list[int],
    rocks: list[int],
    additionalRocks: int,
    expected: int,
) -> None:
    so = Solution()
    actual = so.maximumBags(capacity, rocks, additionalRocks)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 3, 4, 5], [1, 2, 4, 4], 2, 3)

    def test_2(self):
        test(self, [10, 2, 2], [2, 2, 0], 100, 3)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
928 ms
Beats
96.38%
"""
