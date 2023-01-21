import unittest


class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:

        ans: list = []

        def dfs(expr, pos, prev, res):
            if pos == len(num):
                if res == target:
                    ans.append(expr)
                return

            for i in range(pos + 1, len(num) + 1):
                if num[pos] == "0" and i - pos > 1:
                    continue
                n = int(num[pos:i])
                if expr == "":
                    dfs(f"{num[pos: i]}", i, n, res + n)
                else:
                    dfs(f"{expr}+{num[pos: i]}", i, n, res + n)
                    dfs(f"{expr}-{num[pos: i]}", i, -n, res - n)
                    dfs(f"{expr}*{num[pos: i]}", i, n * prev, res - prev + prev * n)

        dfs("", 0, 0, 0)

        return ans


def test(
    testObj: unittest.TestCase, num: str, target: int, expected: list[str]
) -> None:

    so = Solution()
    actual = so.addOperators(num, target)
    actual.sort()
    print(actual)
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "123", 6, ["1*2*3", "1+2+3"])

    def test_2(self):
        test(self, "232", 8, ["2*3+2", "2+3*2"])

    def test_3(self):
        test(self, "3456237490", 9191, [])

    def test_4(self):
        test(self, "1010", 100, ["10*10"])

    def test_6(self):
        test(self, "1234", 10, ["1*2*3+4", "1+2+3+4"])

    def test_7(self):
        test(self, "1", 1, ["1"])

    def test_8(self):
        test(self, "10", 10, ["10"])

    def test_9(self):
        test(self, "100", 10, ["10+0", "10-0"])

    def test_10(self):
        test(self, "105", 5, ["1*0+5", "10-5"])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
754 ms
Beats
95.92%
"""
