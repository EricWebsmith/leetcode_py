import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d: dict = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                ans = [d[complement], i]
                return ans
            d[num] = i

        return []


def test(
    testObj: unittest.TestCase, nums: list[int], target: int, expected: int
) -> None:
    so = Solution()
    actual = so.twoSum(nums, target)
    testObj.assertEqual(actual, expected)


class LC1Tests(unittest.TestCase):
    def test_1(self):
        test(self, [2, 7, 11, 15], 9, [0, 1])

    def test_2(self):
        test(self, [3, 2, 4], 6, [1, 2])

    def test_3(self):
        test(self, [3, 3], 6, [0, 1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
61 ms
Beats
92.97%
"""
