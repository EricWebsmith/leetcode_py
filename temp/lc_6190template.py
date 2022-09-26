from heapq import heappop, heappush
import unittest
from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k==1:
            return list(range(1, n-1))
        left = [0] * n
        current = 1
        index = 1
        while index <= n-k:
            if nums[index] <= nums[index-1]:
                current += 1
            else:
                current = 1

            if current >= k:
                left[index] = 1

            index += 1

        print(left)

        right = [0] * n
        current = 1
        index = n-2
        while index >= k:
            if nums[index] <= nums[index+1]:
                current += 1
            else:
                current = 1

            if current >= k:
                right[index] = 1

            index -= 1

        print(right)

        ans = []
        for i in range(k, n-k):
            if left[i-1] == 1 and right[i+1] == 1:
                ans.append(i)
        
        return ans

def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:
    s = Solution()
    actual = s.goodIndices(nums, k)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, [2,1,1,1,3,4,1], 2, [2,3])

    def test_2(self):
        test(self, [2,1,1,2], 2, [])

    def test_3(self):
        test(self, [3, 2, 4, 3], 1, [1, 2])

    def test_4(self):
        test(self, [80,20,10,9,3,30,40,50,80,90], 4, [4,5])

    def test_5(self):
        test(self, [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442], 4, [4,5])


if __name__ == '__main__':
    unittest.main()

# Runtime: 741 ms, faster than 91.08% of Python3 online submissions for Course Schedule III.
# Memory Usage: 20.2 MB, less than 29.29% of Python3 online submissions for Course Schedule III.
