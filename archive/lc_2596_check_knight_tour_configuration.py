import unittest


class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        location_dict: dict[int, tuple[int, int]] = {}
        for r in range(m):
            for c in range(n):
                location_dict[grid[r][c]] = (r, c)

        privous = location_dict[0]
        if privous != (0, 0):
            return False
        
        for location in range(1, m * n):
            current = location_dict[location]
            diff = (abs(current[0] - privous[0]), abs(current[1] - privous[1]))
            if diff == (1, 2) or diff == (2, 1):
                privous = location_dict[location]

            else:
                return False

        return True


def test(testObj: unittest.TestCase, grid: list[list[int]], expected: bool) -> None:
    so = Solution()
    actual = so.checkValidGrid(grid)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]],
            True,
        )

    def test_2(self):
        test(self, [[0, 3, 6], [5, 8, 1], [2, 7, 4]], False)


    def test_3(self):
        test(self, [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]], False)

if __name__ == "__main__":
    unittest.main()


"""
Runtime
76 ms
Beats
100%
"""
