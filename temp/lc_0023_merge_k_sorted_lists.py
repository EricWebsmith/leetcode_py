import unittest
from heapq import heappop, heappush
from typing import List, Optional

from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        h: List[int] = []
        for list_index in range(k):
            if lists[list_index]:
                heappush(h, (lists[list_index].val, list_index))
                lists[list_index] = lists[list_index].next

        prehead = ListNode(-1)
        current = prehead
        while h:
            v, list_index = heappop(h)
            current.next = ListNode(v)
            current = current.next
            if lists[list_index]:
                heappush(h, (lists[list_index].val, list_index))
                lists[list_index] = lists[list_index].next

        return prehead.next


def test(testObj: unittest.TestCase, arrs: List[List[int]], expected: Optional[ListNode]) -> None:
    heads = [array_to_listnode(arr) for arr in arrs]
    so = Solution()
    actual_root = so.mergeKLists(heads)
    actual = listnode_to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])

    def test_2(self):
        test(self,   [], [])

    def test_3(self):
        test(self,   [[]], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
108 ms
Beats
93.50%
'''
