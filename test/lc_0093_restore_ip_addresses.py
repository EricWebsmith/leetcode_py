import re
import unittest


def _valid_part(part: str) -> bool:
    return re.match(r"^([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$", part) is not None


class Solution:
    def __init__(self) -> None:
        self._s = ""
        self._path = []
        self._ans = []

    def _dfs(self, i: int):
        if len(self._path) == 3:
            if _valid_part(self._s[i:]):
                ip = ".".join(self._path) + "." + self._s[i:]
                self._ans.append(ip)
            return

        for length in range(1, max(3, len(self._s) - i) + 1):
            part = self._s[i : i + length]
            if _valid_part(part):
                self._path.append(part)
                self._dfs(i + length)
                self._path.pop()

    def restoreIpAddresses(self, s: str) -> list[str]:
        self._s = s
        self._dfs(0)
        return self._ans


def test(testObj: unittest.TestCase, s: str, expected: list[str]) -> None:
    so = Solution()
    actual = so.restoreIpAddresses(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "25525511135", ["255.255.11.135", "255.255.111.35"])

    def test_2(self):
        test(self, "0000", ["0.0.0.0"])

    def test_3(self):
        test(
            self,
            "101023",
            ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"],
        )


if __name__ == "__main__":
    unittest.main()


"""

"""
