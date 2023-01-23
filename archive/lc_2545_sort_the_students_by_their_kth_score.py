import unittest


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        score.sort(key=lambda s: -s[k])
        return score


def test(
    testObj: unittest.TestCase,
    score: list[list[int]],
    k: int,
    expected: list[list[int]],
) -> None:
    so = Solution()
    actual = so.sortTheStudents(score, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]],
            2,
            [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]],
        )

    def test_2(self):
        test(self, [[3, 4], [5, 6]], 0, [[5, 6], [3, 4]])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
453 ms
Beats
82.35%
"""
