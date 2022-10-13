from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next


def array_to_listnode(arr: List[int]) -> ListNode:
    n = len(arr)
    head = ListNode(arr[0])
    current = head
    for i in range(1, n):
        next = ListNode(arr[i])
        current.next = next
        current = next

    return head


def listnode_to_array(head: ListNode) -> List[int]:
    arr = []
    current = head
    while current != None:
        arr.append(current.val)
        current = current.next
    return arr
