import unittest
from heapq import heappop, heappush
from typing import Dict, List, Set


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        neighbor_dict: Dict[int, Set] = {v: set() for v in range(n)}
        for a, b, w in edges:
            neighbor_dict[a].add((b, w))
            neighbor_dict[b].add((a, w))

        min_n_cities = n
        ans = n-1

        for i in range(n-1, -1, -1):
            visited = [distanceThreshold+1] * n
            # q = [(distance, city)]
            q = [(0, i)]
            visited[i] = 0
            n_cities = 0
            while q:
                dist, city = heappop(q)
                for neighbor, w in neighbor_dict[city]:
                    new_dist = dist + w
                    if new_dist > distanceThreshold:
                        continue
                    if new_dist >= visited[neighbor]:
                        continue

                    heappush(q, (new_dist, neighbor))  # type: ignore

                    if visited[neighbor] == distanceThreshold+1:
                        n_cities += 1
                    visited[neighbor] = new_dist

                if n_cities >= min_n_cities:
                    break

            if n_cities >= min_n_cities:
                continue

            print(i, n_cities)
            min_n_cities = n_cities
            ans = i

        return ans


def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], distanceThreshold: int, expected: int) -> None:

    so = Solution()

    actual = so.findTheCity(n, edges, distanceThreshold)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   4,  [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],  4, 3)

    def test_2(self):
        test(self,   5,  [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],  2, 0)

    def test_3(self):
        test(self,   2,  [[0, 1, 2]],  2, 1)

    def test_4(self):
        test(self,   5,  [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1], [0, 3, 2]],  2, 2)

    def test_5(self):
        test(self,   5,  [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1], [0, 2, 2]],  2, 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 322 ms, faster than 96.76%
Memory Usage: 15.3 MB, less than 39.37%
'''
