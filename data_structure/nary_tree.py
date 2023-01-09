from queue import Queue
from typing import List


class Node:
    def __init__(self, val=None, children=None) -> None:
        self.val = val
        self.children: list[Node] = children if children is not None else []

    def __repr__(self) -> str:
        return str(self.val)


def node_to_array(root: Node) -> List[int]:
    q = Queue[Node]()

    q.put(root)
    arr = [root.val, None]
    qSize = q.qsize()
    while qSize > 0:
        for i in range(qSize):
            n: Node = q.get()

            for child in n.children:
                arr.append(child.val)
                q.put(child)
            arr.append(None)
        qSize = q.qsize()
    # trim
    while arr[-1] is None:
        arr = arr[:-1]
    return arr


def array_to_node(arr: List[int]) -> Node:
    q = Queue[Node]()
    root = Node(arr[0])
    q.put(root)
    qSize = q.qsize()
    index = 2
    while qSize > 0 and index < len(arr):
        for i in range(qSize):
            n: Node = q.get()
            while index < len(arr) and arr[index] is not None:
                subNode = Node(arr[index])
                n.children.append(subNode)
                q.put(subNode)
                index += 1
            index += 1
        qSize = q.qsize()
    return root
