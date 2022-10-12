from sortedcontainers import SortedList
import unittest
from typing import List


class MaxStack:

    def __init__(self):
        self.value_index = SortedList()
        self.index_value = SortedList()
        self.index = 0

    def push(self, x: int) -> None:
        self.value_index.add((x, self.index))
        self.index_value.add((self.index, x))
        self.index += 1

    def pop(self) -> int:
        index, value = self.index_value.pop()
        self.value_index.remove((value, index))
        return value

    def top(self) -> int:
        return self.index_value[-1][1]

    def peekMax(self) -> int:
        return self.value_index[-1][0]

    def popMax(self) -> int:
        value, index = self.value_index.pop()
        self.index_value.remove((index, value))
        return value


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MaxStack(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "push":
                actual = obj.push(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "pop":
                actual = obj.pop(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "top":
                actual = obj.top(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "peekMax":
                actual = obj.peekMax(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "popMax":
                actual = obj.popMax(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"], [
             [], [5], [1], [5], [], [], [], [], [], []], [None, None, None, None, 5, 5, 1, 5, 1, 5])

    def test_2(self):
        test(self, ["MaxStack", "push", "peekMax", "pop"],
             [[], [5], [], []], [None, None, 5, 5])


if __name__ == '__main__':
    unittest.main()

'''
896ms, 73.91%
'''
