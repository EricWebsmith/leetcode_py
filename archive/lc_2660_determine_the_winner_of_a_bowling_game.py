import unittest


def get_score(player_scores: list[int]):
    pin = 1
    score = 0
    pre = 0
    for p in player_scores:
        score += p * pin
        if pre == 10 or p == 10:
            pin = 2
        else: 
            pin = 1
        pre = p

    return score


class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        score1 = get_score(player1)
        score2 = get_score(player2)

        if score1 > score2:
            return 1

        if score1 < score2:
            return 2

        return 0


def test(testObj: unittest.TestCase, player1: list[int], player2: list[int], expected: int) -> None:
    so = Solution()
    actual = so.isWinner(player1, player2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [4, 10, 7, 9], [6, 5, 2, 3], 1)

    def test_2(self):
        test(self, [3, 5, 7, 6], [8, 10, 10, 2], 2)

    def test_3(self):
        test(self, [2, 3], [4, 1], 0)

    def test_4(self):
        test(self, [5, 6, 1, 10], [5, 1, 10, 5], 2)


    def test_5(self):
        test(self, [9,7,10,7], [10,2,4,10], 1)

if __name__ == "__main__":
    unittest.main()


"""

"""
