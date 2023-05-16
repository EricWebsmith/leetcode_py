import unittest


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = []
        ans2 = []
        for num in set1:
            if num not in set2:
                ans1.append(num)

        for num in set2:
            if num not in set1:
                ans2.append(num)

        return [ans1, ans2]


def test(testObj: unittest.TestCase, nums1: list[int], nums2: list[int], expected: list[list[int]]) -> None:
    so = Solution()
    actual = so.findDifference(nums1, nums2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]])

    def test_2(self):
        test(self, [1, 2, 3, 3], [1, 1, 2, 2], [[3], []])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
183 ms
Beats
57.61%
"""
