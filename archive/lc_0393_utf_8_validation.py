import unittest
from typing import List


class Solution:
    """
    The idea is to compare if the value is in range,
    So we do not need string conversion or bitwise operations.
    It is just simply use the > and < operations.

    Author:
    https://github.com/EricWebsmith/leetcode_py
    """

    def validUtf8(self, data: List[int]) -> bool:
        # firstly, we convert int to binary
        # so in the following code, we do not need to worry about this any more.
        _10000000 = 128
        _11000000 = 128 + 64
        _11100000 = 128 + 64 + 32
        _11110000 = 128 + 64 + 32 + 16
        _11111000 = 128 + 64 + 32 + 16 + 8
        n = len(data)
        i = 0
        while i < n:
            # 0xxxxxxx
            if data[i] < _10000000:
                i += 1
            # 110xxxxx 10xxxxxx
            # if data[i] is in [_11000000, _11100000), we know the first three bits are 110
            elif _11000000 <= data[i] < _11100000:
                i += 1
                for j in range(1):
                    if i >= n:
                        return False
                    # if data[i] < 10000000, the first two bits are not 10.
                    # if data[i] >= 11000000, the first two bits are not 10.
                    # it is invalid and we return false.
                    if data[i] < _10000000 or data[i] >= _11000000:
                        return False
                    i += 1
            # 1110xxxx 10xxxxxx 10xxxxxx
            elif _11100000 <= data[i] < _11110000:
                i += 1
                for j in range(2):
                    if i >= n:
                        return False
                    if data[i] < _10000000 or data[i] >= _11000000:
                        return False
                    i += 1
            # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
            #
            elif _11110000 <= data[i] < _11111000:
                i += 1
                for j in range(3):
                    if i >= n:
                        return False
                    if data[i] < _10000000 or data[i] >= _11000000:
                        return False
                    i += 1
            else:
                return False

        return True


def test(testObj: unittest.TestCase, data: List[int], expected: bool) -> None:
    so = Solution()
    actual = so.validUtf8(data)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [197, 130, 1], True)

    def test_2(self):
        test(self, [235, 140, 4], False)

    # 0xxxxxxx
    def test_3(self):
        test(self, [0, 0, 0], True)

    # 110xxxxx 10xxxxxx
    def test_4(self):
        test(self, [192, 128], True)

    # 111xxxxx 10xxxxxx 10xxxxxx
    def test_5(self):
        test(self, [224, 128, 128], True)

    # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    def test_6(self):
        test(self, [240, 128, 128, 128], True)

    # 0xxxxxxx false
    def test_7(self):
        test(self, [0, 0, 192], False)

    # 110xxxxx 10xxxxxx false
    def test_8(self):
        test(self, [192, 192], False)

    # 111xxxxx 10xxxxxx 10xxxxxx false
    def test_9(self):
        test(self, [224, 128, 192], False)

    # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx false
    def test_10(self):
        test(self, [240, 128, 128, 192], False)

    # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx false
    def test_11(self):
        test(self, [240, 192, 128, 128], False)

    # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx false
    def test_12(self):
        test(self, [240, 128, 192, 128], False)

    # 0xxxxxxx
    def test_13(self):
        test(self, [128, 0, 0], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 142 ms, faster than 78.65%
Memory Usage: 14.1 MB, less than 96.64%
"""
