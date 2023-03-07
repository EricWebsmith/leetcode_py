import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        dp = [""] * (n)
        dp[0] = "1"
        dp[1] = "11"
        for i in range(2, n):
            count = 1
            previous = dp[i - 1][0]
            for c in dp[i - 1][1:]:
                if c == previous:
                    count += 1
                else:
                    dp[i] += str(count) + previous
                    count = 1
                    previous = c
            dp[i] = dp[i] + str(count) + previous
        return dp[-1]


def test(testObj: unittest.TestCase, n: int, expected: str) -> None:
    so = Solution()
    actual = so.countAndSay(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 1, "1")

    def test_4(self):
        test(self, 4, "1211")

    def test_10(self):
        test(self, 10, "13211311123113112211")

    def test_15(self):
        test(
            self,
            15,
            "311311222113111231131112132112311321322112111312211312111322212311322113212221",
        )

    def test_20(self):
        test(
            self,
            20,
            "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211",  # noqa
        )  # noqa


if __name__ == "__main__":
    unittest.main()

"""
Runtime
27 ms
Beats
99.98%
"""
