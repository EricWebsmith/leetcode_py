import unittest
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power = 0
        powers = []
        while n > 0:
            mask = 1 << power
            if n & mask > 0:
                powers.append(mask)
                n -= mask
            # else:
            #     powers.append(0)
            power += 1

        ans = []
        for start, end in queries:
            c = 1
            for i in range(start, end+1):
                c *= powers[i]
            ans.append(c % 1_000_000_007)

        return ans


def test(testObj: unittest.TestCase, n: int, queries: List[List[int]], expected: List[int]) -> None:

    so = Solution()

    actual = so.productQueries(n, queries)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   15,  [[0, 1], [2, 2], [0, 3]], [2, 4, 64])

    def test_2(self):
        test(self,   2,  [[0, 0]], [2])

    def test_3(self):
        test(self,   919,
             [[5, 5], [4, 4], [0, 1], [1, 5], [4, 6], [6, 6], [5, 6], [0, 3], [5, 5], [5, 6], [1, 2], [3, 5], [3, 6],
              [5, 5], [4, 4], [1, 1], [2, 4], [4, 5], [4, 4], [5, 6], [0, 4], [3, 3], [0, 4], [0, 5], [4, 4], [5, 5],
              [4, 6], [4, 5], [0, 4], [6, 6], [6, 6], [6, 6], [2, 2], [0, 5], [1, 4], [0, 3], [2, 4], [5, 5], [6, 6],
              [2, 2], [2, 3], [5, 5], [0, 6], [3, 3], [6, 6], [4, 4], [0, 0], [0, 2], [6, 6], [6, 6], [3, 6], [0, 4],
              [6, 6], [2, 2], [4, 6]],
             [256, 128, 2, 4194304, 16777216, 512, 131072, 128, 256, 131072, 8, 524288, 268435456, 256, 128, 2, 8192,
              32768, 128, 131072, 16384, 16, 16384, 4194304, 128, 256, 16777216, 32768, 16384, 512, 512, 512, 4,
              4194304, 16384, 128, 8192, 256, 512, 4, 64, 256, 147483634, 16, 512, 128, 1, 8, 512, 512, 268435456,
              16384, 512, 4, 16777216]
             )


if __name__ == '__main__':
    unittest.main()

'''

'''
