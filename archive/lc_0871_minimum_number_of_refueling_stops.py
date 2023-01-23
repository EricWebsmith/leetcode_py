# from heapq import heappop, heappush
import heapq
import unittest


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        pq: list[int] = []
        stations.append([target, 1_000_000_000])
        tank = startFuel

        ans = 0
        prev_location = 0
        for location, capacity in stations:
            tank -= location - prev_location
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1

            heapq.heappush(pq, -capacity)  # type: ignore
            prev_location = location

        return ans


def test(
    testObj: unittest.TestCase,
    target: int,
    startFuel: int,
    stations: list[list[int]],
    expected: int,
) -> None:

    s = Solution()
    actual = s.minRefuelStops(target, startFuel, stations)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, 1, 1, [], 0)

    def test_2(self):
        test(self, 100, 1, [[10, 100]], -1)

    def test_3(self):
        test(self, 100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
119 ms
Beats
93.41%
"""
