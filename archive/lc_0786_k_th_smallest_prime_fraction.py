import unittest
from heapq import heappop, heappush
from typing import List, Set, Tuple


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        visited: Set[Tuple[int, int]] = set()
        left = 0
        right = n - 1

        minHeap: List[Tuple] = [(arr[0]/arr[n-1], 0, n-1)]
        visited.add((0, n-1))

        while k and left < right and minHeap:
            _, left, right = heappop(minHeap)
            result = [arr[left], arr[right]]
            if (left+1, right) not in visited:
                heappush(
                    minHeap, (arr[left+1] / arr[right], left+1, right))  # type: ignore
                visited.add((left+1, right))
            if (left, right-1) not in visited:
                heappush(
                    minHeap, (arr[left] / arr[right-1], left, right-1))  # type: ignore
                visited.add((left, right-1))

            k -= 1

        return result


def test(testObj: unittest.TestCase, arr: List[int], k: int, expected: List[int]) -> None:

    so = Solution()

    actual = so.kthSmallestPrimeFraction(arr, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 5],  3, [2, 5])

    def test_2(self):
        test(self,   [1, 7],  1, [1, 7])

    def test_3(self):
        test(self,   [1, 7, 23, 29, 47], 8, [23, 47])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 3952 ms, faster than 23.22%
Memory Usage: 89.5 MB, less than 25.00%
'''

# # TLE
# class Fraction:
#     def __init__(self, numerator: int, denominator: int) -> None:
#         self.numerator: int = numerator
#         self.denominator: int = denominator

#     def __lt__(self, another: 'Fraction'):
#         return self.numerator * another.denominator < another.numerator * self.denominator

#     def __repr__(self) -> str:
#         return f'{self.numerator} / {self.denominator}'
