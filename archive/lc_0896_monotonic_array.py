import unittest


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return True
    
        increasing = True
        if nums[0] > nums[-1]:
            increasing = False

        for i in range(1, len(nums)):
            if increasing:
                if nums[i-1] > nums[i]:
                    return False
            else:
                if nums[i-1] < nums[i]:
                    return False

        return True


def test(testObj: unittest.TestCase, nums: list[int], expected: bool) -> None:
    so = Solution()
    actual = so.isMonotonic(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,2,3], True)

    def test_2(self):
        test(self,   [6,5,4,4], True)

    def test_3(self):
        test(self,   [1,3,2], False)


if __name__ == '__main__':
    unittest.main()


'''
802ms
Beats 88.50%of users with Python3
'''
