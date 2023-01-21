import unittest


class Solution:
    def pushDominoes(self, dominoe_str: str) -> str:
        dominoes = list(dominoe_str)
        n = len(dominoes)
        i = 0
        while i < n:
            if dominoes[i] != ".":
                j = i + 1
                while j < n and dominoes[j] == ".":
                    j += 1

                if j == n:
                    break

                if dominoes[i] == dominoes[j]:
                    dominoes[i : j + 1] = [dominoes[i]] * (j - i + 1)

                if dominoes[i] == "R" and dominoes[j] == "L":
                    left = i + 1
                    right = j - 1
                    while left < right:
                        dominoes[left] = "R"
                        dominoes[right] = "L"

                        left += 1
                        right -= 1

                i = j
            else:
                i += 1
        # left
        i = 0
        while i < n - 1 and dominoes[i] == ".":
            i += 1

        if dominoes[i] == "L":
            dominoes[:i] = ["L"] * i

        # right
        i = n - 1
        while i > 0 and dominoes[i] == ".":
            i -= 1

        if dominoes[i] == "R":
            dominoes[i:] = ["R"] * (n - i)

        return "".join(dominoes)


def test(testObj: unittest.TestCase, dominoes: str, expected: str) -> None:
    so = Solution()
    actual = so.pushDominoes(dominoes)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "RR.L", "RR.L")

    def test_2(self):
        test(self, ".L.R...LR..L..", "LL.RR.LLRRLL..")

    def test_3(self):
        test(self, "LL.RR.LLRRLL..", "LL.RR.LLRRLL..")

    def test_4(self):
        test(self, "L...", "L...")

    def test_5(self):
        test(self, "R...", "RRRR")

    def test_6(self):
        test(self, "...L", "LLLL")

    def test_7(self):
        test(self, "...R", "...R")

    def test_8(self):
        test(self, ".", ".")

    def test_9(self):
        test(self, "R", "R")

    def test_10(self):
        test(self, "L", "L")


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 507 ms, faster than 57.48%
Memory Usage: 15.8 MB, less than 83.88%
"""
