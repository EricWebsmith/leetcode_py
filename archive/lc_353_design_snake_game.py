from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.n = width
        self.m = height
        self.food = food
        self.food_index = 0
        self.head = (0, 0)
        self.body = deque([(0, 0)])

    def move(self, direction: str) -> int:
        r, c = self.head
        new_r, new_c = r, c
        match direction:
            case 'U':
                new_r = new_r - 1
            case 'D':
                new_r = new_r + 1
            case 'L':
                new_c = new_c - 1
            case 'R':
                new_c = new_c + 1

        if new_r == -1 or new_r == self.m or new_c == -1 or new_c == self.n:
            return -1

        eat_food = False
        if self.food_index < len(self.food) and new_r == self.food[self.food_index][0] and new_c == self.food[self.food_index][1]:
            self.food_index += 1
            eat_food = True

        if not eat_food:
            self.body.popleft()
        if (new_r, new_c) in self.body:
            return -1
        self.body.append((new_r, new_c))
        self.head = (new_r, new_c)
        return self.food_index


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = SnakeGame(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "move":
                actual = obj.move(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["SnakeGame", "move", "move", "move", "move", "move", "move"], [[3, 2, [
             [1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]], [None, 0, 0, 1, 1, 2, -1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 344 ms, faster than 66.90% of Python3 online submissions for Design Snake Game.
Memory Usage: 15.8 MB, less than 51.61% of Python3 online submissions for Design Snake Game.
'''
