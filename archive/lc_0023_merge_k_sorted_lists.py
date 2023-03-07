import unittest
from heapq import heappop, heappush

from leetcode_data_structure.link_list import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        k = len(lists)
        h: list[tuple[int, int]] = []
        for list_index in range(k):
            if lists[list_index] is not None:
                heappush(h, (lists[list_index].val, list_index))  # type: ignore
                lists[list_index] = lists[list_index].next  # type: ignore

        prehead = ListNode(-1)
        current = prehead
        while h:
            v, list_index = heappop(h)  # type: ignore
            current.next = ListNode(v)
            current = current.next
            if lists[list_index] is not None:
                heappush(h, (lists[list_index].val, list_index))  # type: ignore
                lists[list_index] = lists[list_index].next  # type: ignore

        return prehead.next


def test(testObj: unittest.TestCase, arrs: list[list[int]], expected: ListNode | None) -> None:
    heads = [ListNode.from_array(arr) for arr in arrs]
    so = Solution()
    actual_root = so.mergeKLists(heads)
    actual = ListNode.to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])

    def test_2(self):
        test(self, [], [])

    def test_3(self):
        test(self, [[]], [])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
108 ms
Beats
93.50%
"""
