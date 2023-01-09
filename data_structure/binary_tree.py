from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

    def __repr__(self) -> str:
        return str(self.val)


def array_to_treenode(arr: List[int]) -> TreeNode | None:
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    for i in range(1, len(arr), 2):
        node = q.popleft()
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        if i+1 < len(arr) and arr[i+1] is not None:
            node.right = TreeNode(arr[i+1])
            q.append(node.right)

    return root


def treenode_to_array(root: Optional[TreeNode]) -> List[int]:
    q = deque([root])
    arr = []
    while q:
        node = q.popleft()
        if node:
            arr.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            arr.append(None)

    while arr and arr[-1] is None:
        arr.pop()

    return arr


def get_treenode_by_val(root: TreeNode, val: int):
    ans = None

    def dfs(node):
        nonlocal ans
        if node is None:
            return

        if node.val == val:
            ans = node
            return

        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans


def get_treenodes_by_vals(root: TreeNode, vals: List[int]):
    ans = []

    def dfs(node):
        if node is None:
            return

        if node.val in vals:
            ans.append(node)

        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans
