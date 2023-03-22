import unittest
from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        graph: dict = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        min_score = roads[0][2]
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)

        return min_score


def test(testObj: unittest.TestCase, n: int, roads: list[list[int]], expected: int) -> None:
    so = Solution()
    actual = so.minScore(n, roads)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5)

    def test_2(self):
        test(self, 4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2)

    def test_3(self):
        test(self, 4, [[1, 2, 2], [1, 3, 4], [3, 4, 7], [2, 4, 1]], 1)

    def test_4(self):
        test(self, 4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7], [3, 4, 1]], 1)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
1617 ms
Beats
93.96%
"""
