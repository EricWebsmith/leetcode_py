import unittest
from typing import List, Optional


class SegmentNode:
    def __init__(self, low: int, high: int, count: int) -> None:
        self.low = low
        self.high = high
        self.split = -1
        self.count = count
        self.left: Optional[SegmentNode] = None
        self.right: Optional[SegmentNode] = None

    def __repr__(self) -> str:
        return f'[{self.low}, {self.high}], {self.count}'


class MyCalendarThree:

    def __init__(self) -> None:
        self.root = SegmentNode(0, 10**9, 0)
        self.k = 0

    def book(self, start: int, end: int) -> int:
        self.add(start, end, self.root)
        return self.k

    def add(self, start: int, end: int, node: SegmentNode):
        if node.split != -1:
            if end <= node.split:
                self.add(start, end, node.left)  # type: ignore
            elif start >= node.split:
                self.add(start, end, node.right)  # type: ignore
            else:
                self.add(start, node.split, node.left)  # type: ignore
                self.add(node.split, end, node.right)  # type: ignore
            return

        if start == node.low and end == node.high:
            node.count += 1
            self.k = max(self.k, node.count)
        elif start == node.low:
            node.split = end
            node.left = SegmentNode(node.low, node.split, node.count + 1)
            node.right = SegmentNode(node.split, node.high, node.count)
            self.k = max(self.k, node.count+1)
        elif end == node.high:
            node.split = start
            node.left = SegmentNode(node.low, node.split, node.count)
            node.right = SegmentNode(node.split, node.high, node.count + 1)
            self.k = max(self.k, node.count+1)
        else:
            node.split = start
            node.left = SegmentNode(node.low, node.split, node.count)
            node.right = SegmentNode(node.split, node.high, node.count)
            self.add(start, end, node.right)


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MyCalendarThree(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "book":
                actual = obj.book(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MyCalendarThree", "book", "book", "book", "book", "book", "book"], [
             [], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]], [None, 1, 1, 2, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()

'''
264ms, 98.46%
'''
