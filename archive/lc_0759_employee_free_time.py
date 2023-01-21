import unittest


class Interval:
    def __init__(self, start: int | None = None, end: int | None = None):
        self.start: int | None = start
        self.end: int | None = end


class Solution:
    def employeeFreeTime(self, schedule: list[list[Interval]]) -> list[Interval]:

        hq: list[list] = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                hq.append([schedule[i][j].start, schedule[i][j].end])

        hq.sort()

        prev_end = -1
        ans: list = []
        while len(hq) > 0:
            first = hq.pop(0)
            if first[0] > prev_end:
                ans.append(Interval(prev_end, first[0]))

            prev_end = max(prev_end, first[1])

        return ans[1:]


def test(
    testObj: unittest.TestCase, schedule_arr: list[list[list[int]]], expected: int
) -> None:

    schedule: list = []
    for i in range(len(schedule_arr)):
        person: list = []
        for j in range(len(schedule_arr[i])):
            person.append(
                Interval(start=schedule_arr[i][j][0], end=schedule_arr[i][j][1])
            )
        schedule.append(person)
    so = Solution()
    actual_arr = so.employeeFreeTime(schedule)
    actual: list = []
    for i in range(len(actual_arr)):
        actual.append([actual_arr[i].start, actual_arr[i].end])
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]], [[3, 4]])

    def test_2(self):
        test(self, [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]], [[5, 6], [7, 9]])

    def test_3(self):
        test(
            self,
            [
                [[7, 24], [29, 33], [45, 57], [66, 69], [94, 99]],
                [[6, 24], [43, 49], [56, 59], [61, 75], [80, 81]],
                [[5, 16], [18, 26], [33, 36], [39, 57], [65, 74]],
                [[9, 16], [27, 35], [40, 55], [68, 71], [78, 81]],
                [[0, 25], [29, 31], [40, 47], [57, 87], [91, 94]],
            ],
            [[26, 27], [36, 39], [87, 91]],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 95 ms, faster than 91.67%
Memory Usage: 15.7 MB, less than 78.36%
"""
