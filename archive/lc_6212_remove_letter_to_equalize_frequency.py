import unittest
from typing import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        values = list(c.values())
        m = max(values)
        m_count = 0
        m_1_count = 0
        for v in values:
            if v == m:
                m_count += 1
            elif v == m - 1:
                m_1_count += 1
            else:
                return False

        if m_count == 1:
            return True

        if m_1_count == 0 and values[0] == 1:
            return True

        if m_1_count == 1:
            return True

        return False


def test(testObj: unittest.TestCase, word: str, expected: bool) -> None:
    so = Solution()
    actual = so.equalFrequency(word)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abcc", True)

    def test_2(self):
        test(self,   "aazz", False)

    def test_3(self):
        test(self,   "bac", True)

    def test_4(self):
        test(self,   "abbcc", True)


if __name__ == '__main__':
    unittest.main()

'''

'''
