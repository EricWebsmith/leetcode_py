import unittest

from leetcode_data_structure import TreeNode, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        middle = self.find_middle(head)

        root = TreeNode(middle.val)

        root.right = self.sortedListToBST(middle.next)
        middle.next = None
        root.left = self.sortedListToBST(head)
        
        return root

    # it is guarenteed to have a middle by sortedListToBST
    def find_middle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next  # type: ignore
            prev = slow
            slow = slow.next  # type: ignore

        prev.next = None  # type: ignore
        return slow  # type: ignore


def test(testObj: unittest.TestCase, head_arr: list[int], expected: list[int]) -> None:
    head = ListNode.from_array(head_arr)
    so = Solution()
    actual_root = so.sortedListToBST(head)
    actual = TreeNode.to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [-10,-3,0,5,9], [0,-3,9,-10,None,5])

    def test_2(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()


'''
Runtime
110 ms
Beats
98.76%
'''
