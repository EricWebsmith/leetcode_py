import unittest


class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        mask = 1

        ans = [0, 0]
        odd_even = 0
        while n > 0:
            if n & mask == mask:
                ans[odd_even] += 1
                n = n - mask

            mask = mask << 1
            odd_even = 1 - odd_even

        return ans


def test(testObj: unittest.TestCase, n: int, expected: list[int]) -> None:
    so = Solution()
    actual = so.evenOddBit(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 17, [2, 0])

    def test_2(self):
        test(self, 2, [0, 1])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
36 ms
Beats
100%
"""
