import unittest


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])
        root: dict = dict()
        for word in words:
            current = root
            for ch in word:
                if ch not in current:
                    current[ch] = dict()
                current = current[ch]
            current["$"] = word

        ans: list = []

        def backtrack(r: int, c: int, node: dict, path: list[tuple[int, int]]):
            if len(node) == 0:
                return

            if r == -1 or r == m or c == -1 or c == n:
                return
            if len(path) == 11:
                return
            if (r, c) in path:
                return

            ch = board[r][c]
            if ch not in node:
                return

            path.append((r, c))

            current = node[ch]

            if "$" in current:
                ans.append(current["$"])
                del current["$"]

            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_r = r + dr
                new_c = c + dc

                backtrack(new_r, new_c, current, path)

            if not current:
                del node[ch]
            path.pop()

        for r in range(m):
            for c in range(n):
                backtrack(r, c, root, [])

        return ans


def test(
    testObj: unittest.TestCase,
    board: list[list[str]],
    words: list[str],
    expected: list[str],
) -> None:
    so = Solution()
    actual = so.findWords(board, words)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        )

    def test_2(self):
        test(self, [["a", "b"], ["c", "d"]], ["abcb"], [])

    def test_3(self):
        test(
            self,
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain", "takh"],
            ["eat", "oath", "takh"],
        )

    def test_4(self):
        test(
            self,
            [
                ["o", "a", "b", "n"],
                ["o", "t", "a", "e"],
                ["a", "h", "k", "r"],
                ["a", "f", "l", "v"],
            ],
            ["oa", "oaa"],
            ["oa", "oaa"],
        )

    def test_5(self):
        test(
            self,
            [
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ],
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1999 ms, faster than 61.41%
Memory Usage: 15.5 MB, less than 73.89%
"""
