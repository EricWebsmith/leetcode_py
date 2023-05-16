import unittest


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = - sign
        
        return sign


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.arraySign(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [-1,-2,-3,-4,3,2,1], 1)

    def test_2(self):
        test(self,   [1,5,0,2,-3], 0)

    def test_3(self):
        test(self,   [-1,1,-1,1,-1], -1)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
64 ms
Beats
44.77%
'''
