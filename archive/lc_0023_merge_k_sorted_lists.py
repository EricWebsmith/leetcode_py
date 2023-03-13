from heapq import heappop, heappush
import unittest
from leetcode_data_structure import ListNode


class Solution:
    def mergeKLists(self, heads: list[ListNode | None]) -> ListNode | None:
        h: list[tuple[int, int]] = []
        for i, head in enumerate(heads):
            if head is not None:
                heappush(h, (head.val, i))
                heads[i] = head.next
        
        prehead = ListNode(0)
        current = prehead
        while len(h) > 0:
            v, i = heappop(h)
            head = heads[i]
            if head is not None:
                heappush(h, (head.val, i))
                heads[i] = head.next

            listNode = ListNode(v)
            current.next = listNode
            current = current.next

        return prehead.next


def test(testObj: unittest.TestCase, arrs: list[list[int]], expected: list[int]) -> None:
    so = Solution()
    heads = [ListNode.from_array(arr) for arr in arrs]
    actual_root = so.mergeKLists(heads)
    actual = ListNode.to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6])

    def test_2(self):
        test(self,   [], [])

    def test_3(self):
        test(self,   [[]], [])


if __name__ == '__main__':
    unittest.main()


'''
Runtime
103 ms
Beats
76.36%
'''
