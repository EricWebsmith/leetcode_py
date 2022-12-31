import unittest


class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        cur_max = 0
        for coin in coins:
            if coin == 1:
                cur_max += coin
            elif coin <= cur_max + 1:
                cur_max += coin
            else:
                break

        return cur_max + 1


def test(testObj: unittest.TestCase, coins: list[int], expected: int) -> None:

    so = Solution()
    actual = so.getMaximumConsecutive(coins)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3], 2)

    def test_2(self):
        test(self,   [1, 1, 1, 4], 8)

    def test_3(self):
        test(self,   [1, 4, 10, 3, 1], 20)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
788 ms
Beats
81.51%
'''
