import unittest
from heapq import heappop, heappush
from typing import Any, Dict, List, Set


def get_bidirectional_edges(vetices: List, from_to_times: List[List]) -> Dict[Any, Set]:
    edges = {v: set() for v in vetices}
    for from_, to_, time in from_to_times:
        edges[from_].add((to_, time))
        edges[to_].add((from_, time))

    return edges


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        MAX_TIME = 1_000_000_000
        MAX_FEE = 1_000_000_000
        n = len(passingFees)
        edge_dict = get_bidirectional_edges(list(range(n)), edges)
        # q = [(fee, time, city)]
        q = [[passingFees[0], 0, 0]]

        dp = [[MAX_FEE, MAX_TIME] for i in range(n)]
        dp[0] = [passingFees[0], 0]
        while q:
            fee, time, city = heappop(q)
            if time > maxTime:
                continue
            if city == n - 1:
                return fee

            for next_city, next_time in edge_dict[city]:
                next_fee = passingFees[next_city]
                previous_fee, previous_time = dp[next_city]
                if fee + next_fee < previous_fee or time+next_time < previous_time:
                    heappush(q, [fee+next_fee, time+next_time, next_city])
                    dp[next_city] = [fee+next_fee, time+next_time]

        return -1


def test(testObj: unittest.TestCase, maxTime: int, edges: List[List[int]],
         passingFees: List[int], expected: int) -> None:
    so = Solution()
    actual = so.minCost(maxTime, edges, passingFees)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   30,  [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1],
             [3, 4, 10], [4, 5, 15]],  [5, 1, 2, 20, 20, 3], 11)

    def test_2(self):
        test(self,   29,  [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1],
             [3, 4, 10], [4, 5, 15]],  [5, 1, 2, 20, 20, 3], 48)

    def test_3(self):
        test(self,   25,  [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1],
             [3, 4, 10], [4, 5, 15]],  [5, 1, 2, 20, 20, 3], -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 410 ms, faster than 94.57%
Memory Usage: 15 MB, less than 21.72%
'''
