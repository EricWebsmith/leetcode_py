import unittest
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        basket = dict()
        left = 0
        right = 0
        basket[fruits[0]] = 1
        ans = 1
        while left <= right and right < n:
            if len(basket) <= 2:
                ans = max(ans, right - left + 1)
                right += 1
                if right == n:
                    break
                basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            elif len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

        return ans


def test(testObj: unittest.TestCase, fruits: List[int], expected: int) -> None:

    so = Solution()

    actual = so.totalFruit(fruits)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 1], 3)

    def test_2(self):
        test(self, [0, 1, 2, 2], 3)

    def test_3(self):
        test(self, [1, 2, 3, 2, 2], 4)

    def test_4(self):
        test(self, [1, 2, 3, 2, 2, 1, 2, 3, 4], 4)

    def test_5(self):
        test(self, [1], 1)

    def test_6(self):
        test(self, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1109 ms
Beats
82.89%
"""
