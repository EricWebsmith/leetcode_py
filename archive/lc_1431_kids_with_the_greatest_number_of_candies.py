import unittest


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        moving_max = max(candies)
        ans = []
        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= moving_max)
        
        return ans


def test(testObj: unittest.TestCase, candies: list[int], extraCandies: int, expected: list[bool]) -> None:
    so = Solution()
    actual = so.kidsWithCandies(candies, extraCandies)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [2,3,5,1,3],  3, [True,True,True,False,True])

    def test_2(self):
        test(self,   [4,2,1,1,2],  1, [True,False,False,False,False])

    def test_3(self):
        test(self,   [12,1,12],  10, [True,False,True])


    def test_4(self):
        test(self,   [2,8,7],  1, [False,True,True])

if __name__ == '__main__':
    unittest.main()


'''
Runtime
35 ms
Beats
87.18%
'''
