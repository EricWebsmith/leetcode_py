import unittest


class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        mod = 1_000_000_007
        # threshold
        n = len(inventory)

        def balls_by_threshold(threshold):
            balls = 0
            for i in range(n):
                if inventory[i] >= threshold:
                    balls += inventory[i] - threshold + 1
            return balls

        # first false
        left = 1
        right = max(inventory)
        while left < right:
            m = (left + right) // 2
            balls = balls_by_threshold(m)
            if balls > orders:
                left = m + 1
            else:
                right = m

        balls = balls_by_threshold(left)
        income = (orders - balls) * (left - 1) % mod
        for i in range(n):
            if inventory[i] >= left:
                income += ((inventory[i] + left) * (inventory[i] - left + 1)) >> 1 % mod

        income = income % mod

        return income


def test(testObj: unittest.TestCase, inventory: list[int], orders: int, expected: int) -> None:

    so = Solution()
    actual = so.maxProfit(inventory, orders)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [2, 5], 4, 14)

    def test_2(self):
        test(self, [3, 5], 6, 19)

    def test_3(self):
        test(self, [1, 2], 1, 2)

    def test_4(self):
        test(self, [773160767], 252264991, 70267492)

    def test_5(self):
        test(self, [497978859, 167261111, 483575207, 591815159], 836556809, 373219333)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1300 ms
Beats
60.11%
"""
