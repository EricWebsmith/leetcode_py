import unittest


class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        def clock_wise(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        trees.sort()
        upper: list = []
        lower: list = []
        for t in trees:
            while len(upper) > 1 and clock_wise(upper[-2], upper[-1], t) > 0:
                upper.pop()
            while len(lower) > 1 and clock_wise(lower[-2], lower[-1], t) < 0:
                lower.pop()

            upper.append(tuple(t))
            lower.append(tuple(t))

        return [[x, y] for (x, y) in set(upper + lower)]


def test(testObj: unittest.TestCase, trees: list[list[int]], expected: list[list[int]]) -> None:
    so = Solution()
    actual = so.outerTrees(trees)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]],
        )

    def test_2(self):
        test(self, [[1, 2], [2, 2], [4, 2]], [[4, 2], [2, 2], [1, 2]])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
665 ms
Beats
46.99%
"""
