from heapq import heappop, heappush
import unittest
from functools import cache
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from data_structure.link_list import ListNode, listnode_to_array, array_to_listnode


class MyHashMap:

    def __init__(self):
        

    def put(self, key: int, value: int) -> None:
        

    def get(self, key: int) -> int:
        

    def remove(self, key: int) -> None:
        



        pass

def test(testObj: unittest.TestCase, actions:list, params:list , expected:list) -> None:
    n = len(actions)
    obj = MyHashMap(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            
            case "put":
                obj.put(*params[i])
            case "get":
                get_actual = obj.get(*params[i])
                testObj.assertEqual(get_actual, expected[i])
            case "remove":
                obj.remove(*params[i])


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self, ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"], [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]], [None, None, None, 1, -1, None, 1, None, -1])


if __name__ == '__main__':
    unittest.main()


'''

'''
