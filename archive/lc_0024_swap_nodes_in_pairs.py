import unittest
from leetcode_data_structure import ListNode


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        prehead = ListNode(0)
        prehead.next = head
        current: ListNode | None = prehead
        while current and current.next and current.next.next:
            a = current.next
            b = current.next.next
            c = current.next.next.next
            current.next = b
            b.next = a
            a.next = c
            current = a

        return prehead.next


def test(testObj: unittest.TestCase, head_arr: list[int], expected: list[int]) -> None:
    head = ListNode.from_array(head_arr)
    so = Solution()
    actual_root = so.swapPairs(head)
    actual = ListNode.to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3,4], [2,1,4,3])

    def test_2(self):
        test(self,   [], [])

    def test_3(self):
        test(self,   [1], [1])

    def test_4(self):
        test(self,   [1, 2], [2, 1])


if __name__ == '__main__':
    unittest.main()


'''

'''
