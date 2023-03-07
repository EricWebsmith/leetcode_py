import unittest
from leetcode_data_structure.binary_tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        current = [root]
        ans: list[list[int]] = []
        odd = True 
        while current:
            if odd:
                ans.append([node.val for node in current])
            else:
                ans.append([node.val for node in current[::-1]])

            newCurrent: list[TreeNode] = []
            for node in current:
                if node.left:
                    newCurrent.append(node.left)
                if node.right:
                    newCurrent.append(node.right)
            
            odd = not odd
            current = newCurrent
        
        return ans


def test(testObj: unittest.TestCase, root_arr: list[int | None], expected:list[list[int]]) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.zigzagLevelOrder(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [3,9,20,None,None,15,7], [[3],[20,9],[15,7]])

    def test_2(self):
        test(self,   [1], [[1]])

    def test_3(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()


'''
Runtime
28 ms
Beats
92.86%
'''
