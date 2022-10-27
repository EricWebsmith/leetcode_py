import unittest
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        for dr in range(n):
            for dc in range(n):
                # right, down
                new_ans = 0
                for r in range(dr, n):
                    for c in range(dc, n):
                        shifted = img1[r-dr][c-dc]
                        if shifted == 1 and shifted == img2[r][c]:
                            new_ans += 1
                ans = max(ans, new_ans)

                # left, down
                new_ans = 0
                for r in range(dr, n):
                    for c in range(n - dc):
                        shifted = img1[r-dr][c+dc]
                        if shifted == 1 and shifted == img2[r][c]:
                            new_ans += 1
                ans = max(ans, new_ans)

                # right, up
                new_ans = 0
                for r in range(n - dr):
                    for c in range(dc, n):
                        shifted = img1[r+dr][c-dc]
                        if shifted == 1 and shifted == img2[r][c]:
                            new_ans += 1
                ans = max(ans, new_ans)

                # left, up
                new_ans = 0
                for r in range(n - dr):
                    for c in range(n - dc):
                        shifted = img1[r+dr][c+dc]
                        if shifted == 1 and shifted == img2[r][c]:
                            new_ans += 1
                ans = max(ans, new_ans)
        return ans


def test(testObj: unittest.TestCase, img1: List[List[int]], img2: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.largestOverlap(img1, img2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
             [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3)

    def test_2(self):
        test(self,   [[1]],  [[1]], 1)

    def test_3(self):
        test(self,   [[0]],  [[0]], 0)

    def test_4(self):
        test(self,   [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
748 ms
Beats
73.10%
'''
