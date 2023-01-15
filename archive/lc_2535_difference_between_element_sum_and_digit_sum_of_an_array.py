import unittest


def digit_sum(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num = num // 10
    return ans


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        dsum = sum(digit_sum(n) for n in nums)
        return abs(element_sum-dsum)


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.differenceOfSum(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 15, 6, 3], 9)

    def test_2(self):
        test(self,   [1, 2, 3, 4], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
121 ms
Beats
100%
'''
