import unittest
from collections import defaultdict
from typing import List, Optional

from leetcode_data_structure import TreeNode

null = None


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths: dict[str, list] = defaultdict(list)
        heights = defaultdict(int)

        def dfs(node: TreeNode, d: int) -> int:
            if node is None:
                return -1

            depths[node.val] = d  # type: ignore
            h = max(dfs(node.left, d + 1), dfs(node.right, d + 1)) + 1  # type: ignore
            heights[node.val] = h
            return h

        dfs(root, 0)  # type: ignore

        levels = defaultdict(list)
        for val, d in depths.items():
            levels[d].append((-heights[val], val))
            levels[d].sort()

            if len(levels[d]) > 2:
                levels[d].pop()

        ans: list = []
        for q in queries:
            d = depths[q]  # type: ignore
            if len(levels[d]) == 1:
                ans.append(d - 1)  # type: ignore
            elif levels[d][0][1] == q:
                ans.append(-levels[d][1][0] + d)  # type: ignore
            else:
                ans.append(-levels[d][0][0] + d)  # type: ignore

        return ans


def test(
    testObj: unittest.TestCase,
    root_arr: List[int | None],
    queries: List[int],
    expected: List[int],
) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.treeQueries(root, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7], [4], [2])

    def test_2(self):
        test(self, [5, 8, 9, 2, 1, 3, 7, 4, 6], [3, 2, 4, 8], [3, 2, 3, 2])

    def test_3(self):
        test(self, [1, 2], [2], [0])

    def test_4(self):
        test(self, [1, null, 5, 3, null, 2, 4], [3, 5, 4, 2, 4], [1, 0, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1184 ms
Beats
100%
"""
