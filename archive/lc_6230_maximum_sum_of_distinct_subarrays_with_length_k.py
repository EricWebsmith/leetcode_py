import unittest
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        for i in range(k):
            d[nums[i]] += 1

        ans = 0
        s = sum(nums[0:k])
        if len(d) == k:
            ans = max(ans, s)

        last = k
        while last < n:

            # pop
            prev = last - k
            if d[nums[prev]] == 1:
                del d[nums[prev]]
            else:
                d[nums[prev]] -= 1

            if nums[last] in d:
                d[nums[last]] += 1
            else:
                d[nums[last]] = 1

            s = s - nums[prev] + nums[last]

            if len(d) == k:
                ans = max(ans, s)

            last = last + 1

        return ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()
    actual = so.maximumSubarraySum(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 5, 4, 2, 9, 9, 9],  3, 15)

    def test_2(self):
        test(self,   [4, 4, 4],  3, 0)

    def test_3(self):
        nums = [i for i in range(1, 100000)]
        k = 50000
        test(self,   nums,  k, 3749975000)


if __name__ == '__main__':
    unittest.main()

'''

'''
