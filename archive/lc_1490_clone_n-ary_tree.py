
import unittest

from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        newRoot = Node(root.val)
        for child in root.children:
            newRoot.children.append(self.cloneTree(child))

        return newRoot


def test(testObj: unittest.TestCase, rootArr: list[int], expected: int) -> None:
    root = array_to_node(rootArr)
    s = Solution()
    actualRoot = s.cloneTree(root)
    actual = node_to_array(actualRoot)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [1, None, 3, 2, 4, None, 5, 6], [1, None, 3, 2, 4, None, 5, 6])

    def test_2(self):
        test(self,  [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None,
                     11, None, 12, None, 13, None, None, 14],
             [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None,
              12, None, 13, None, None, 14])


if __name__ == '__main__':
    unittest.main()

"""
Runtime
77 ms
Beats
80.40%
"""
