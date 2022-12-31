import json
import unittest
from collections import deque
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'{self.val}'


def treenode_to_array(root: TreeNode) -> List[int]:
    # BFS
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


def array_to_treenode(arr: List[int]) -> TreeNode:
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


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        arr = treenode_to_array(root)
        return str(arr).replace('None', 'null')

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.replace('None', 'null')
        arr = json.loads(data)
        return array_to_treenode(arr)


def test(testObj: unittest.TestCase, root_arr: List[int], expected: None) -> None:
    so = Codec()
    data = str(root_arr)
    root = so.deserialize(data)
    actual_str = so.serialize(root)
    actual = json.loads(actual_str)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5])

    def test_2(self):
        test(self,   [], [])

    def test_3(self):
        test(self,   [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
299 ms
Beats
73.91%
'''
