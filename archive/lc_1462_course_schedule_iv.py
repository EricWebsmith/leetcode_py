import unittest


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        edge_dict: dict[int, set] = {v: set() for v in range(n)}
        for pre, post in prerequisites:
            edge_dict[post].add(pre)

        visited = [False] * n

        def dfs(v):
            if visited[v]:
                return edge_dict[v]
            for child in list(edge_dict[v]):
                descendants = dfs(child)
                for d in descendants:
                    edge_dict[v].add(d)
            visited[v] = True
            return edge_dict[v]

        for v in range(n):
            dfs(v)
            visited[v] = True

        ans: list = []
        for pre, post in queries:
            ans.append(pre in edge_dict[post])

        return ans


def test(
    testObj: unittest.TestCase,
    numCourses: int,
    prerequisites: list[list[int]],
    queries: list[list[int]],
    expected: list[bool],
) -> None:
    so = Solution()
    actual = so.checkIfPrerequisite(numCourses, prerequisites, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 2, [[1, 0]], [[0, 1], [1, 0]], [False, True])

    def test_2(self):
        test(self, 2, [], [[1, 0], [0, 1]], [False, False])

    def test_3(self):
        test(self, 3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True])

    def test_4(self):
        test(
            self,
            7,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
            [[0, 4], [2, 3], [6, 5]],
            [True, True, False],
        )

    def test_5(self):
        test(
            self,
            8,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
            [[0, 4], [2, 3], [6, 5], [5, 7]],
            [True, True, False, False],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 773 ms, faster than 95.76%
Memory Usage: 17.7 MB, less than 43.97%
"""
