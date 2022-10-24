from bisect import bisect_left
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import random
null = None
true = True
false = False


class RandomizedCollection:

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        index = bisect_left(self.arr, val)
        ans = not(index < len(self.arr) and self.arr[index] == val)
        self.arr.insert(index, val)
        return ans

    def remove(self, val: int) -> bool:

        index = bisect_left(self.arr, val)
        if index == len(self.arr) or self.arr[index] != val:
            return False

        del self.arr[index]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = RandomizedCollection(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insert":
                actual = obj.insert(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "remove":
                actual = obj.remove(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "getRandom":
                actual = obj.getRandom(*params[i])
                # testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"], [
             [], [1], [1], [2], [], [1], []], [None, True, False, True, 2, True, 1])

    def test_2(self):
        test(self, ["RandomizedCollection", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
             [[], [1], [2], [2], [], [1], [2], []],
             [null, true, false, true, 2, true, false, 2])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 457 ms, faster than 94.39% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 64.6 MB, less than 95.77% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
'''
