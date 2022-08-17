from tkinter.tix import Tree
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_treenode(arr: List[int]) -> TreeNode:
    root = TreeNode(arr[0])
    q = [root]
    l = len(q)
    index = 1

    while l>0 and index<len(arr):
        for i in range(0, l):
            node = q.pop(0)

            if node == None:
                continue

            if arr[index] == None:
                node.left = None
            else:
                node.left = TreeNode(arr[index])
            q.append(node.left)
            index+=1

            if index==len(arr):
                break

            if arr[index] == None:
                node.right = None
            else:
                node.right = TreeNode(arr[index])
            q.append(node.right)
            index+=1

            if index==len(arr):
                break
        l = len(q)
    
    return root

def treenode_to_array(root: Optional[TreeNode]) -> List[int]:
    q = [root]
    arr = []
    while len(q)>0:
        for i in range(0, len(q)):
            node = q.pop(0)
            if node is None:
                arr.append(None)
            else:
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)

    while arr[-1] == None:
        arr = arr[:-1]

    return arr