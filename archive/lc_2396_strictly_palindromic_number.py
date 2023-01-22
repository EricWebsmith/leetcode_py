import unittest


def is_palindrome(n: int, base: int) -> bool:
    if n % base == 0:
        return False

    bits: list[bool] = []
    while n > 0:
        bits.append(n % base == 1)
        n = n // base

    left = 0
    right = len(bits) - 1
    while left < right:
        if bits[left] != bits[right]:
            return False
        left += 1
        right -= 1

    return True


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 2 + 1):
            if not is_palindrome(n, base):
                return False

        return True


def test(testObj: unittest.TestCase, n: int, expected: bool) -> None:
    so = Solution()
    actual = so.isStrictlyPalindromic(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 9, False)

    def test_2(self):
        test(self, 4, False)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
35 ms
Beats
62.9%
"""
