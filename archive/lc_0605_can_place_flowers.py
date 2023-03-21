import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        
        length = len(flowerbed)
        for i in range(length):
            if (flowerbed[i]==0) and (i == 0 or flowerbed[i-1] == 0) and (i==length-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        
        return False


def test(testObj: unittest.TestCase, flowerbed: list[int], n: int, expected: bool) -> None:
    so = Solution()
    actual = so.canPlaceFlowers(flowerbed, n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,0,0,0,1],  1, True)

    def test_2(self):
        test(self,   [1,0,0,0,1],  2, False)

    def test_3(self):
        test(self,   [0],  1, True)

if __name__ == '__main__':
    unittest.main()


'''
Runtime
163 ms
Beats
78.96%
'''
