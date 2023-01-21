import unittest
from typing import List, Optional

from data_structure.link_list import ListNode, array_to_listnode, listnode_to_array


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prehead.next = head

        slow = prehead
        fast = prehead

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        slow.next = slow.next.next
        return prehead.next


def test(
    testObj: unittest.TestCase, head_arr: List[int], expected: Optional[ListNode]
) -> None:
    head = array_to_listnode(head_arr)
    so = Solution()

    actual_root = so.deleteMiddle(head)
    actual = listnode_to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6])

    def test_2(self):
        test(self, [1, 2, 3, 4], [1, 2, 4])

    def test_3(self):
        test(self, [2, 1], [2])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1909 ms
Beats
89.72%
"""
