import unittest
from typing import List


class StockSpanner:

    def __init__(self):
        self.arr = [1_000_000]
        self.hop = [-1]

    def next(self, price: int) -> int:
        self.arr.append(price)
        n = len(self.arr)
        prev = n-2
        while self.arr[prev] <= price:
            prev = self.hop[prev]

        self.hop.append(prev)
        return n - 1 - prev


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = StockSpanner(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            case "next":
                actual = obj.next(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"], [
             [], [100], [80], [60], [70], [60], [75], [85]], [None, 1, 1, 1, 2, 1, 4, 6])

    def test_2(self):
        test(self,
             ["StockSpanner", "next", "next", "next", "next", "next"],
             [[], [31], [41], [48], [59], [79]],
             [None, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 448 ms, faster than 89.53% of Python3 online submissions for Online Stock Span.
Memory Usage: 19.7 MB, less than 7.77% of Python3 online submissions for Online Stock Span.
'''
