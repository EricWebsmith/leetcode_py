import unittest

from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


def test(testObj: unittest.TestCase, head_arr: ListNode, node_val: int, expected: ListNode) -> None:
    head = array_to_listnode(head_arr)
    node = head
    while node.val != node_val:
        node = node.next
    so = Solution()
    so.deleteNode(node)
    actual = listnode_to_array(head)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 5, 1, 9],  5, [4, 1, 9])

    def test_2(self):
        test(self,   [4, 5, 1, 9],  1, [4, 5, 9])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
41 ms
Beats
93.61%
'''
