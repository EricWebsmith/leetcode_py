
import unittest
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(0, len(nums)):
            self.dict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for key, value in self.dict.items():
            if key in vec.dict:
                ans += self.dict[key] * vec.dict[key]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


def test(testObj: unittest.TestCase, nums1: List[int], nums2: List[int], expected: int) -> None:
    s1 = SparseVector(nums1)
    s2 = SparseVector(nums2)
    actual = s1.dotProduct(s2)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [1, 0, 0, 2, 3],  [0, 3, 0, 4, 0], 8)

    def test_2(self):
        test(self,  [0, 1, 0, 0, 0],  [0, 0, 0, 0, 2], 0)

    def test_3(self):
        test(self,  [0, 1, 0, 0, 2, 0, 0],  [1, 0, 0, 0, 3, 0, 4], 6)


if __name__ == '__main__':
    unittest.main()
