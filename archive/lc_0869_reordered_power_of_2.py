import unittest
from typing import List


class Solution:
    def is_reorder(self, ai: int, b: List[str]):
        a = list(str(ai))
        if len(a) != len(b):
            return False

        a.sort()

        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True

    def reorderedPowerOf2(self, n: int) -> bool:
        # for i in range(0, 31):
        #     print(2 ** i, end=', ')

        two = [
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            1024,
            2048,
            4096,
            8192,
            16384,
            32768,
            65536,
            131072,
            262144,
            524288,
            1048576,
            2097152,
            4194304,
            8388608,
            16777216,
            33554432,
            67108864,
            134217728,
            268435456,
            536870912,
            1073741824,
        ]

        if n < 0:
            n = -n

        s = list(str(n))
        s.sort()

        return any([self.is_reorder(i, s) for i in two])


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.reorderedPowerOf2(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 1, True)

    def test_2(self):
        test(self, 10, False)

    def test_3(self):
        test(self, 46, True)

    def test_4(self):
        test(self, 2048, True)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 42 ms, faster than 84.49%
Memory Usage: 13.9 MB, less than 64.17%
"""
