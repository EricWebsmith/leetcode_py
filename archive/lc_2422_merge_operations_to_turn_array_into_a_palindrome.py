import unittest


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        left_sum = nums[0]
        right_sum = nums[n-1]
        left = 0
        right = n - 1
        n_operations = 0
        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += nums[left]
                n_operations += 1
            elif left_sum > right_sum:
                right -= 1
                right_sum += nums[right]
                n_operations += 1
            else:
                left += 1
                left_sum += nums[left]
                right -= 1
                right_sum += nums[right]

        return n_operations


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.minimumOperations(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 3, 2, 1, 2, 3, 1], 2)

    def test_2(self):
        test(self,   [1, 2, 3, 4], 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
879 ms
Beats
98.57%
'''
