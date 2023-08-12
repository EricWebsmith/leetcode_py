import unittest


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        coins.sort()
        dp = [1] + [0] * (amount)
        for coin in coins:
            next_dp = [1] + [0] * (amount)
            for i in range(1, amount + 1):
                next_dp[i] = dp[i]  # not use coin

                remain = i - coin
                if remain >= 0:
                    next_dp[i] += next_dp[remain]  # use coin
            dp = next_dp
        return dp[amount]


def test(testObj: unittest.TestCase, amount: int, coins: list[int], expected: int) -> None:
    so = Solution()
    actual = so.change(amount, coins)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   5,  [1, 2, 5], 4)

    def test_2(self):
        test(self,   3,  [2], 0)

    def test_3(self):
        test(self,   10,  [10], 1)


if __name__ == '__main__':
    unittest.main()


'''
223ms
Beats 71.15%of users with Python3
'''
