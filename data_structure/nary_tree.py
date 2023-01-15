from collections import deque


class Node:
    def __init__(self, val=None, children=None) -> None:
        self.val = val
        self.children: list[Node] = children if children is not None else []

    def __repr__(self) -> str:
        return str(self.val)


def node_to_array(root: Node) -> list[int]:
    q = deque[Node]()

    q.put(root)
    arr = [root.val, None]
    qSize = len(q)
    while qSize > 0:
        for i in range(qSize):
            n: Node = q.popleft()

            for child in n.children:
                arr.append(child.val)
                q.append(child)
            arr.append(None)
        qSize = len(q)
    # trim
    while arr[-1] is None:
        arr = arr[:-1]
    return arr


def array_to_node(arr: list[int]) -> Node:
    q = deque[Node]()
    root = Node(arr[0])
    q.append(root)
    qSize = len(q)
    index = 2
    while qSize > 0 and index < len(arr):
        for i in range(qSize):
            n: Node = q.popleft()
            while index < len(arr) and arr[index] is not None:
                subNode = Node(arr[index])
                n.children.append(subNode)
                q.append(subNode)
                index += 1
            index += 1
        qSize = len(q)
    return root
