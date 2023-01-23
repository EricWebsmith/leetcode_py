import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        h: list = []
        left = 0
        right = n - 1
        for i in range(candidates):
            if left <= right:
                heappush(h, (costs[i], i))  # type: ignore
                left += 1
            if left <= right:
                heappush(h, (costs[n - 1 - i], n - 1 - i))  # type: ignore
                right -= 1

        ans = 0
        for _ in range(k):
            c, i = heappop(h)
            ans += c
            if left <= right:
                if i < left:
                    heappush(h, (costs[left], left))  # type: ignore
                    left += 1
                elif i > right:
                    heappush(h, (costs[right], right))  # type: ignore
                    right -= 1

        return ans


def test(testObj: unittest.TestCase, costs: List[int], k: int, candidates: int, expected: int) -> None:

    so = Solution()

    actual = so.totalCost(costs, k, candidates)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11)

    def test_2(self):
        test(self, [1, 2, 4, 1], 3, 3, 4)

    def test_3(self):
        test(self, [2, 2, 2, 4, 1], 3, 1, 5)

    def test_4(self):
        test(self, [2, 2, 1, 1, 2], 3, 1, 5)

    def test_5(self):
        test(self, [2, 1, 1, 2, 2], 3, 1, 4)

    def test_6(self):
        test(self, [2, 2, 2, 1, 1, 2, 2], 3, 2, 5)

    def test_7(self):
        test(self, [2, 2, 1, 1, 2, 2, 2], 3, 2, 4)

    def test_8(self):
        test(
            self,
            [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
            11,
            2,
            423,
        )

    def test_9(self):
        test(self, [7, 2, 9, 2, 0, 2, 1, 9, 2], 3, 2, 5)


if __name__ == "__main__":
    unittest.main()

"""

"""
