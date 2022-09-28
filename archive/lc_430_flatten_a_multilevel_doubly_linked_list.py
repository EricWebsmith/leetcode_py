import unittest
from typing import Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            first = node
            last = node
            while node != None:
                last = node
                next = node.next
                if node.child:
                    child_first, child_last = dfs(node.child)
                    last = child_last
                    if next:
                        child_last.next = next
                        next.prev = child_last
                    child_first.prev = node
                    node.next = child_first
                node.child = None
                node = next
            return first, last

        dfs(head)

        return head


def test(testObj: unittest.TestCase, head: 'Optional[Node]', expected: int) -> None:

    so = Solution()
    actual = so.flatten(head)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10,
             None, None, 11, 12], [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6])

    def test_2(self):
        test(self,   [1, 2, None, 3], [1, 3, 2])

    def test_3(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 42 ms, faster than 84.79% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.9 MB, less than 43.96% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
'''
