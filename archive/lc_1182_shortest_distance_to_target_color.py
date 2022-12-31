
import unittest
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        d = {}

        for i,  q in enumerate(queries):
            q.append(i)
        queries.sort(key=lambda x: x[0])

        q_index = 0
        ans = [n] * len(queries)
        for i in range(n):
            d[colors[i]] = i
            while q_index < len(queries) and queries[q_index][0] == i:
                previous_index = d.get(queries[q_index][1], -1)
                if previous_index != -1:
                    ans[queries[q_index][2]] = i - previous_index
                q_index += 1

        d = {}
        q_index = len(queries) - 1
        for i in range(n-1, -1, -1):
            d[colors[i]] = i
            while q_index >= 0 and queries[q_index][0] == i:
                previous_index = d.get(queries[q_index][1], -1)
                if previous_index != -1:
                    ans[queries[q_index][2]] = min(ans[queries[q_index][2]], previous_index-i)
                q_index -= 1

        for i in range(len(ans)):
            if ans[i] == n:
                ans[i] = -1

        return ans


def test(testObj: unittest.TestCase, colors: List[int], queries: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.shortestDistanceColor(colors, queries)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, [1, 1, 2, 1, 3, 2, 2, 3, 3],  [[1, 3], [2, 2], [6, 1]], [3, 0, 3])

    def test_2(self):
        test(self, [1, 2],  [[0, 3]], [-1])

    def test_3(self):
        test(self, [2, 1, 2, 2, 1], [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]], [0, -1, -1, 1, 1])


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 2400 ms, faster than 75.99%
Memory Usage: 38.4 MB, less than 10.46%
"""
