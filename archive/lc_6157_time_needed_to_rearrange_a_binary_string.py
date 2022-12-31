
import unittest


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while s.find('01') >= 0:
            s = s.replace('01', '10')
            count += 1

        return count


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.secondsToRemoveOccurrences(s)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  "0110101", 4)

    def test_2(self):
        test(self,  "11100", 0)


if __name__ == '__main__':
    unittest.main()
