import unittest


class Solution:
    def __init__(self) -> None:
        self._s: str = ""
        self._n = 0
        self._ans: list[list[str]] = []
        self._mat: list[list[bool]] = []
        self._path = []

    def is_palindrome(self, start: int, _end: int) -> bool:
        left = start
        right = _end
        while left < right:
            if self._s[left] != self._s[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(self, start):
        if start == self._n:
            self._ans.append([part for part in self._path])

        for _end in range(start, self._n):
            if self._mat[start][_end]:
                self._path.append(self._s[start : _end + 1])
                self.dfs(_end + 1)
                self._path.pop()

    def partition(self, s: str) -> list[list[str]]:
        self._s = s
        self._n = len(s)
        self._mat = [[False for _ in range(self._n)] for _ in range(self._n)]
        for start in range(self._n):
            for _end in range(start, self._n):
                self._mat[start][_end] = self.is_palindrome(start, _end)

        self.dfs(0)

        return self._ans


def test(testObj: unittest.TestCase, s: str, expected: list[list[str]]) -> None:
    so = Solution()
    actual = so.partition(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "aab", [["a", "a", "b"], ["aa", "b"]])

    def test_2(self):
        test(self, "a", [["a"]])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
663 ms
Beats
83.49%
"""
