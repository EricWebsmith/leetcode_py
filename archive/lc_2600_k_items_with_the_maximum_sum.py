import unittest


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        
        if k <= numOnes + numZeros:
            return numOnes
        
        return numOnes-(k - numOnes + numZeros)


def test(testObj: unittest.TestCase, numOnes: int, numZeros: int, numNegOnes: int, k: int, expected: int) -> None:
    so = Solution()
    actual = so.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   3,  2,  0,  2, 2)

    def test_2(self):
        test(self,   3,  2,  0,  4, 3)


if __name__ == '__main__':
    unittest.main()


'''

'''
