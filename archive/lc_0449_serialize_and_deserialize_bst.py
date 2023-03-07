import unittest
from typing import List, Optional

from leetcode_data_structure.binary_tree import TreeNode


def array_to_treenode(arr: List[int]) -> TreeNode | None:
    if len(arr) == 0:
        return None

    root = TreeNode(arr[0])
    q: list[TreeNode | None] = [root]
    length = len(q)
    index = 1

    while length > 0 and index < len(arr):
        for i in range(0, length):
            node = q.pop(0)

            if node is None:
                continue

            if arr[index] is None:
                node.left = None
            else:
                node.left = TreeNode(arr[index])
            q.append(node.left)
            index += 1

            if index == len(arr):
                break

            if arr[index] is None:
                node.right = None
            else:
                node.right = TreeNode(arr[index])
            q.append(node.right)
            index += 1

            if index == len(arr):
                break
        length = len(q)

    return root


def treenode_to_array(root: Optional[TreeNode]) -> List[int | None]:
    q = [root]
    arr: list[int | None] = []
    while len(q) > 0:
        for i in range(0, len(q)):
            node = q.pop(0)
            if node is None:
                arr.append(None)
            else:
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)

    while len(arr) > 0 and arr[-1] is None:
        arr = arr[:-1]

    return arr


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        arr = treenode_to_array(root)
        return str(arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        arr = eval(data)
        root = array_to_treenode(arr)
        return root


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)

    so = Codec()
    s = so.serialize(root)
    root2 = so.deserialize(s)
    actual = treenode_to_array(root2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 1, 3], [2, 1, 3])

    def test_2(self):
        test(self, [], [])


if __name__ == "__main__":
    unittest.main()

"""

"""
