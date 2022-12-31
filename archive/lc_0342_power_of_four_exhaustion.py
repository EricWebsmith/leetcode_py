import unittest


class Solution:
    def print4(self):
        arr = []
        for i in range(0, 16):
            arr.append(4**i)

        print(arr)
        # [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216,
        # 67108864, 268435456, 1073741824]

    def isPowerOfFour(self, n: int) -> bool:
        return n in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304,
                     16777216, 67108864, 268435456, 1073741824]


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.isPowerOfFour(n)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  16, True)

    def test_2(self):
        test(self,  5, False)

    def test_3(self):
        test(self,  1, True)


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 25 ms, faster than 99.41%
Memory Usage: 14 MB, less than 10.18%
"""
