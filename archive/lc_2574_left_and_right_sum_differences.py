import unittest


class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        leftSum = [nums[0]]
        for num in nums[1:]:
            leftSum.append(leftSum[-1] + num)
    
        rightSum = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            rightSum.append(rightSum[-1] + nums[i])
        rightSum.reverse()

        ans = []
        for i in range(len(nums)):
            ans.append(abs(leftSum[i] - rightSum[i]))
        

        return ans


def test(testObj: unittest.TestCase, nums: list[int], expected:list[int]) -> None:
    so = Solution()
    actual = so.leftRigthDifference(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [10, 4, 8, 3], [15, 1, 11, 22])

    def test_2(self):
        test(self,   [1], [0])


if __name__ == '__main__':
    unittest.main()


'''
Runtime
69 ms
Beats
93.33%
'''
