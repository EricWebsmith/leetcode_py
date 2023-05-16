import unittest


class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        start = max(nums)
        return (start + start + k - 1) * k // 2


def test(testObj: unittest.TestCase, nums: list[int], k: int, expected: int) -> None:
    so = Solution()
    actual = so.maximizeSum(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3,4,5],  3, 18)

    def test_2(self):
        test(self,   [5,5,5],  2, 11)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
178 ms
Beats
22.22%
'''
