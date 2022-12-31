import unittest
from typing import List, Optional

from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prehead.next = head

        fast_pointer = prehead
        slow_pointer = prehead

        index = 0
        while fast_pointer:
            fast_pointer = fast_pointer.next
            if index > n:
                slow_pointer = slow_pointer.next

            index += 1

        slow_pointer.next = slow_pointer.next.next

        return prehead.next


def test(
    testObj: unittest.TestCase,
    head_arr: List[int],
    n: int,
    expected: Optional[ListNode],
) -> None:
    head = array_to_listnode(head_arr)
    so = Solution()

    actual_root = so.removeNthFromEnd(head, n)
    actual = listnode_to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

    def test_2(self):
        test(self, [1], 1, [])

    def test_3(self):
        test(self, [1, 2], 1, [1])

    def test_4(self):
        test(self, [1, 2, 3, 4, 5], 1, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 31 ms, faster than 97.25%
Memory Usage: 14 MB, less than 20.71%
"""
