import unittest
from typing import Dict, List, Set
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


def top_sort(edges: Dict[int, Set[int]]) -> List[int]:
    stack = []
    visiting = set()
    visited = set()

    cyclic = False

    def dfs(v: int):
        nonlocal cyclic
        if cyclic:
            return

        if v in visited:
            return
        if v in visiting:
            cyclic = True
            return

        if len(edges[v]) == 0:
            stack.append(v)
        else:
            visiting.add(v)
            for child in edges[v]:
                dfs(child)
            stack.append(v)
            visiting.remove(v)

        visited.add(v)

    for v in edges:
        dfs(v)

    if cyclic:
        return []

    stack.reverse()

    return stack


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # convert individual items to one-item group
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        groups = list(range(m))

        betweenGroupEdges: Dict[int, Set[int]] = {g: set() for g in groups}
        inGroupEdges: Dict[int, Dict[int, Set[int]]] = {g: {} for g in groups}
        for i in range(n):
            g = group[i]
            inGroupEdges[g][i] = set()

        for b, beforeItem in enumerate(beforeItems):
            gb = group[b]
            for a in beforeItem:
                ga = group[a]
                if ga == gb:
                    inGroupEdges[ga][a].add(b)
                else:
                    betweenGroupEdges[ga].add(gb)

        group_sort = top_sort(betweenGroupEdges)

        ans = []
        for g in group_sort:
            edges = inGroupEdges[g]
            ians = top_sort(edges)
            if len(ians) != len(edges):
                return []
            ans += ians

        return ans


def test(testObj: unittest.TestCase, n: int, m: int, group: List[int], beforeItems: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.sortItems(n, m, group, beforeItems)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   8,  2,  [-1, -1, 1, 0, 0, 1, 0, -1],  [[], [6],
             [5], [6], [3, 6], [], [], []], [7, 0, 5, 2, 6, 3, 4, 1])

    def test_2(self):
        test(self,   8,  2,  [-1, -1, 1, 0, 0, 1, 0, -1],
             [[], [6], [5], [6], [3], [], [4], []], [])

    def test_3(self):
        test(self,   5, 5, [2, 0, -1, 3, 0],
             [[2, 1, 3], [2, 4], [], [], []], [2, 3, 4, 1, 0])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 538 ms, faster than 77.30% of Python3 online submissions for Sort Items by Groups Respecting Dependencies.
Memory Usage: 46.6 MB, less than 16.22% of Python3 online submissions for Sort Items by Groups Respecting Dependencies.
'''
