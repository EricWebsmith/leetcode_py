import unittest


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        ins = [0] * n
        outs = [0] * n
        for t in trust:
            outs[t[0] - 1] += 1
            ins[t[1] - 1] += 1

        for i in range(n):
            if ins[i] == n - 1 and outs[i] == 0:
                return i + 1

        return -1


def test(testObj: unittest.TestCase, n: int, trust: list[list[int]], expected: int) -> None:
    so = Solution()
    actual = so.findJudge(n, trust)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 2, [[1, 2]], 2)

    def test_2(self):
        test(self, 3, [[1, 3], [2, 3]], 3)

    def test_3(self):
        test(self, 3, [[1, 3], [2, 3], [3, 1]], -1)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
747 ms
Beats
83.90%
"""
