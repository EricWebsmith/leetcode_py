import sys
import unittest
from heapq import heappop, heappush


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        MOD = 1_000_000_007
        distances_to_last_node = [sys.maxsize] * n
        edge_dict = {v: set() for v in range(n)}
        for a, b, d in edges:
            edge_dict[a-1].add((b-1, d))
            edge_dict[b-1].add((a-1, d))

        q = [(0, n-1)]
        distances_to_last_node[n-1] = 0
        while q:
            d, v = heappop(q)
            for next_v, v_to_next in edge_dict[v]:
                next_dist = d + v_to_next
                if next_dist < distances_to_last_node[next_v]:
                    distances_to_last_node[next_v] = next_dist
                    heappush(q, (next_dist, next_v))  # type: ignore

        print(distances_to_last_node)

        cache = dict()

        def dfs(v):
            if v == n - 1:
                return 1

            if v in cache:
                return cache[v]
            ans = 0
            for neighbor, d in edge_dict[v]:
                if distances_to_last_node[v] > distances_to_last_node[neighbor]:
                    ians = dfs(neighbor)
                    if ians > 0:
                        ans = ans + ians
                        ans = ans % MOD
            cache[v] = ans
            return ans

        return dfs(0)


def test(testObj: unittest.TestCase, n: int, edges: list[list[int]], expected: int) -> None:
    so = Solution()
    actual = so.countRestrictedPaths(n, edges)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   5,  [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]], 3)

    def test_2(self):
        test(self,   7,  [[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2], [7, 5, 3], [2, 6, 4]], 1)

    def test_3(self):
        test(self,   2,  [[1, 2, 3]], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2261 ms
Beats
75%
'''
