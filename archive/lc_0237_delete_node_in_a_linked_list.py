import unittest

from leetcode_data_structure import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        if node.next:
            node.val = node.next.val
            node.next = node.next.next


def test(testObj: unittest.TestCase, head_arr: list[int], node_val: int, expected: ListNode) -> None:
    head = ListNode.from_array(head_arr)
    assert head is not None
    node: ListNode = head
    while node.val != node_val:
        node = node.next  # type: ignore
    so = Solution()
    so.deleteNode(node)
    actual = ListNode.to_array(head)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [4, 5, 1, 9], 5, [4, 1, 9])

    def test_2(self):
        test(self, [4, 5, 1, 9], 1, [4, 5, 9])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
41 ms
Beats
93.61%
"""
