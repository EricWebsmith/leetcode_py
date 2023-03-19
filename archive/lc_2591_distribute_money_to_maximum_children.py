import unittest


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # distribute 1 dollar to each child
        money -= children

        if money < 0:
            return -1

        # continue giving each child 7 dollars
        sevens = money // 7

        # everyone gets 7
        if children * 7 == money:
            return children

        # everyone but the last one gets 7, the last one gets 3
        if (children - 1) * 7 + 3 == money:
            return children - 2

        # do not have enough money
        if money < children * 7:
            return money // 7

        # too much money
        return children - 1


def test(testObj: unittest.TestCase, money: int, children: int, expected: int) -> None:
    so = Solution()
    actual = so.distMoney(money, children)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 20, 3, 1)

    def test_2(self):
        test(self, 16, 2, 2)

    def test_3(self):
        test(self, 1, 2, -1)

    def test_4(self):
        test(self, 2, 2, 0)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
52 ms
Beats
100%
"""
