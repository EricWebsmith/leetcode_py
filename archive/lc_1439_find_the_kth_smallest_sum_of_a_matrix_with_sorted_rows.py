import unittest
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        indices0 = tuple([0] * m)
        s0 = sum([mat[r][0] for r in range(m)])
        q = [(s0, indices0)]
        heapify(q)

        visited = set()
        while q:
            s, indices = heappop(q)
            if indices in visited:
                continue
            visited.add(indices)
            k -= 1
            if k == 0:
                return s
            for r in range(m):
                new_indices = [*indices]
                new_indices[r] += 1
                if new_indices[r] == n:
                    continue
                new_s = s + mat[r][new_indices[r]] - mat[r][indices[r]]
                heappush(q, (new_s, tuple(new_indices)))  # type: ignore

        return -1


def test(testObj: unittest.TestCase, mat: List[List[int]], k: int, expected: int) -> None:

    so = Solution()

    actual = so.kthSmallest(mat, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 3, 11], [2, 4, 6]],  5, 7)

    def test_2(self):
        test(self,   [[1, 3, 11], [2, 4, 6]],  9, 17)

    def test_3(self):
        test(self,   [[1, 10, 10], [1, 4, 5], [2, 3, 6]],  7, 9)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 253 ms, faster than 72.41%
Memory Usage: 18 MB, less than 26.11%
'''
