import unittest


class Solution:

    def trips(self, times: list[int], current_time: int) -> int:
        return sum([current_time // time for time in times])

    def minimumTime(self, times: list[int], total_trips: int) -> int:
        lo = 1
        hi = times[0] * total_trips
        while lo < hi:
            mid = (lo + hi) // 2
            current_total_trips = self.trips(times, mid)
            if current_total_trips < total_trips:
                lo = mid + 1
            else:
                hi = mid

        return lo


def test(testObj: unittest.TestCase, time: list[int], totalTrips: int, expected:int) -> None:
    so = Solution()
    actual = so.minimumTime(time, totalTrips)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3],  5, 3)

    def test_2(self):
        test(self,   [2],  1, 2)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
2333 ms
Beats
62.25%
'''
