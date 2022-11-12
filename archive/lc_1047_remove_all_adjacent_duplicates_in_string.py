import unittest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for c in s:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)

        return ''.join(result)


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:
    so = Solution()
    actual = so.removeDuplicates(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abbaca", "ca")

    def test_2(self):
        test(self,   "azxxzy", "ay")

    def test_3(self):
        test(self,   "aaaaaaaa", "")


if __name__ == '__main__':
    unittest.main()

'''
Runtime
75 ms
Beats
94.8%
'''
