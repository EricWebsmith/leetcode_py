class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: 'ListNode' | None = next


def array_to_listnode(arr: list[int]) -> ListNode | None:
    n = len(arr)
    if n == 0:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, n):
        next = ListNode(arr[i])
        current.next = next
        current = next

    return head


def listnode_to_array(head: ListNode | None) -> list[int]:
    arr: list = []
    current: ListNode | None = head
    while current is not None:
        arr.append(current.val)
        current = current.next
    return arr
