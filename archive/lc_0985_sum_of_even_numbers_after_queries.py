import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s = sum(num for num in nums if num % 2 == 0)
        ans = []
        for i in range(n):
            val, index = queries[i]
            s -= (1 - nums[index] % 2) * nums[index]
            nums[index] += val
            s += (1 - nums[index] % 2) * nums[index]
            ans.append(s)

        return ans


def test(testObj: unittest.TestCase, nums: List[int], queries: List[List[int]], expected:List[int]) -> None:
    
    so = Solution()
    
    actual = so.sumEvenAfterQueries(nums,queries)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3,4],  [[1,0],[-3,1],[-4,0],[2,3]], [8,6,2,4])

    def test_2(self):
        test(self,   [1],  [[4,0]], [0])
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 538 ms, faster than 91.84% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.6 MB, less than 20.41% of Python3 online submissions for Sum of Even Numbers After Queries.
'''
