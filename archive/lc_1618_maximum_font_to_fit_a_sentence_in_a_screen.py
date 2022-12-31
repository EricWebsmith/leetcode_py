import unittest
from typing import List


class FontInfo(object):
    """Return the width of char ch when fontSize is used."""

    def getWidth(self, fontSize, ch):
        """
        :type fontSize: int
        :type ch: char
        :rtype int
        """

    def getHeight(self, fontSize):
        """
        :type fontSize: int
        :rtype int
        """


class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        def fit(m: int):
            moving_width = 0
            c_h = fontInfo.getHeight(m)

            if c_h > h:
                return False

            for c in text:
                c_w = fontInfo.getWidth(m, c)
                moving_width += c_w
                if moving_width > w:
                    return False

            return True

        if not fit(fonts[0]):
            return -1

        left = 0
        right = len(fonts)-1
        while left < right:
            m = (left + right+1) >> 1
            if fit(fonts[m]):
                left = m
            else:
                right = m - 1

        return fonts[left]


def test(testObj: unittest.TestCase, text: str, w: int, h: int,
         fonts: List[int], fontInfo: FontInfo, expected: int) -> None:
    """
    Cannot mimic FontInfo
    """
    # so = Solution()

    # actual = so.maxFont(text,w,h,fonts,fontInfo)

    # testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "helloworld",  80,  20,  [6, 8, 10, 12, 14, 16, 18, 24, 36], None, 6)

    def test_2(self):
        test(self,   "leetcode",  1000,  50,  [1, 2, 4], None, 4)

    def test_3(self):
        test(self,   "easyquestion",  100,  100,  [10, 15, 20, 25], None, -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 606 ms, faster than 95.38%
Memory Usage: 25.9 MB, less than 16.92%
'''
