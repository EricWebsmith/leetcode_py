import unittest


class DSU:
    def __init__(self) -> None:
        self.union_find: list[int] = [i for i in range(26)]

    def union(self, a: str, b: str) -> None:
        index_a = self.find(a)
        index_b = self.find(b)

        if index_a < index_b:
            self.union_find[index_b] = index_a
        else:
            self.union_find[index_a] = index_b

    def find(self, c: str) -> int:
        i = ord(c) - ord("a")
        p = i
        while self.union_find[p] != p:
            p = self.union_find[p]
        self.union_find[i] = p
        return p

    def find_str(self, c: str) -> str:
        i = self.find(c)
        return chr(ord("a") + i)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()
        for c1, c2 in zip(s1, s2):
            dsu.union(c1, c2)

        ans = list[str]()
        for c in baseStr:
            ans.append(dsu.find_str(c))

        return "".join(ans)


def test(testObj: unittest.TestCase, s1: str, s2: str, baseStr: str, expected: str) -> None:

    so = Solution()
    actual = so.smallestEquivalentString(s1, s2, baseStr)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "parker", "morris", "parser", "makkek")

    def test_2(self):
        test(self, "hello", "world", "hold", "hdld")

    def test_3(self):
        test(self, "leetcode", "programs", "sourcecode", "aauaaaaada")


if __name__ == "__main__":
    unittest.main()

"""
Runtime
37 ms
Beats
96.55%
"""
