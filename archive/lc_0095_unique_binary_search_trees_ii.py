import unittest
from leetcode_data_structure import TreeNode


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:

        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]

            res = []
            for val in range(left, right+1):

                for left_tree in generate(left, val-1):
                    for right_tree in generate(val+1, right):
                        root = TreeNode(val, left_tree, right_tree)
                        res.append(root)

            return res
        return generate(1, n)


def test(testObj: unittest.TestCase, n: int, expected_matrix: list[list[int | None]]) -> None:
    so = Solution()
    actual = so.generateTrees(n)
    expected = [TreeNode.from_array(expected_arr) for expected_arr in expected_matrix]
    actual_str_list = [TreeNode.to_array(node) for node in actual]
    expected_str_list = [TreeNode.to_array(node) for node in expected]
    testObj.assertCountEqual(actual_str_list, expected_str_list)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3, [[1, None, 2, None, 3], [1, None, 3, 2], [2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]])

    def test_2(self):
        test(self,   1, [[1]])


if __name__ == '__main__':
    unittest.main()


'''
61ms
Beats 85.76%of users with Python3
'''
