import unittest
from typing import Optional

from leetcode_data_structure import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prehead.next = head

        fast_pointer = prehead
        slow_pointer = prehead

        index = 0
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next  # type: ignore
            if index > n:
                slow_pointer = slow_pointer.next  # type: ignore

            index += 1

        slow_pointer.next = slow_pointer.next.next  # type: ignore

        return prehead.next


def test(
    testObj: unittest.TestCase,
    head_arr: list[int],
    n: int,
    expected: list[int],
) -> None:
    head = ListNode.from_array(head_arr)
    so = Solution()

    actual_root = so.removeNthFromEnd(head, n)
    actual = ListNode.to_array(actual_root)
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
