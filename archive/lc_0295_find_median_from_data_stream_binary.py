import unittest
from bisect import insort_left
from typing import List


class MedianFinder:

    def __init__(self) -> None:
        self.arr: list = []

    def addNum(self, num: int) -> None:
        insort_left(self.arr, num)

    def findMedian(self) -> float:
        length = len(self.arr)
        if length % 2 == 1:
            return self.arr[length//2]
        else:
            return (self.arr[length//2] + self.arr[length//2 - 1])/2


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MedianFinder(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addNum":
                obj.addNum(*params[i])

            case "findMedian":
                actual = obj.findMedian(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [
             [], [1], [2], [], [3], []], [None, None, None, 1.5, None, 2.0])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
1471 ms
Beats
34.8%
'''
