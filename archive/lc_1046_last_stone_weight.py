from heapq import heappop, heappush, heapify

import unittest


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) >=2:
            a = heappop(stones)
            b = heappop(stones)
            c = abs(a-b)
            if c>0:
                heappush(stones, -c)
        
        if len(stones) == 1:
            return -stones[0]

        return 0


def test(testObj: unittest.TestCase, stones: list[int], expected: int) -> None:
    so = Solution()
    actual = so.lastStoneWeight(stones)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [2,7,4,1,8,1], 1)

    def test_2(self):
        test(self,   [1], 1)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
32 ms
Beats
70.98%
'''
