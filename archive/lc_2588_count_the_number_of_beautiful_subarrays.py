import unittest
from collections import defaultdict


class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        s = 0
        for num in nums:
            s ^= num
            ans += d[s]
            d[s] += 1

        return ans


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.beautifulSubarrays(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [4,3,1,2,4], 2)

    def test_2(self):
        test(self,   [1,10,4], 0)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
1050 ms
Beats
100%
'''
