import unittest


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(m):
            ans = m
            five = 5
            while five <= m:
                ans += m // five
                five *= 5

            return ans

        # left and right are divide by 5 already.
        left = k * 4 // 5
        right = k
        while left < right + 1:
            m = (left + right) >> 1
            zeros = f(m)
            if zeros == k:
                return 5
            elif zeros < k:
                left = m + 1
            else:
                right = m - 1

        return 0


def test(testObj: unittest.TestCase, k: int, expected: int) -> None:

    so = Solution()
    actual = so.preimageSizeFZF(k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 0, 5)

    def test_2(self):
        test(self, 5, 0)

    def test_3(self):
        test(self, 3, 5)

    def test_4(self):
        test(self, 1_000_000_000, 5)

    def test_5(self):
        test(self, 1_000_000, 5)

    def test_6(self):
        test(self, 1_000, 5)

    def test_7(self):
        test(self, 17, 0)

    def test_8(self):
        test(self, 18, 5)

    def test_9(self):
        test(self, 23, 0)

    def test_10(self):
        test(self, 45, 5)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 26 ms, faster than 98.93%
Memory Usage: 14 MB, less than 16.04%
"""
