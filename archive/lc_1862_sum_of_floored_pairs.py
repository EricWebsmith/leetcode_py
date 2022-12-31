import unittest
from typing import Counter, List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        counts = Counter(nums)
        keys = list(counts.keys())
        keys.sort()
        n = len(keys)

        ans = 0
        for i in range(n):
            ci = counts[keys[i]]
            ans += ci * ci
            ans = ans % MOD
            for j in range(i+1, n):
                cj = counts[keys[j]]
                floor = keys[j] // keys[i]

                ans += floor * ci * cj
                ans = ans % MOD

        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()
    actual = so.sumOfFlooredPairs(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 5, 9], 10)

    def test_2(self):
        test(self,   [7, 7, 7, 7, 7, 7, 7], 49)


if __name__ == '__main__':
    unittest.main()

'''

'''
