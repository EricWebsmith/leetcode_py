import unittest


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i1 = 0
        i2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            if nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1

        return -1


def test(testObj: unittest.TestCase, nums1: list[int], nums2: list[int], expected: int) -> None:
    so = Solution()
    actual = so.getCommon(nums1, nums2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3], [2, 4], 2)

    def test_2(self):
        test(self, [1, 2, 3, 6], [2, 3, 4, 5], 2)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
461 ms
Beats
88.40%
"""
