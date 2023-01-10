import unittest
from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict: dict = dict()
        t_dict: dict = dict()

        def get_code(c: str, d: Dict[str, int]):
            code = -1
            if c in d:
                code = d[c]
            else:
                code = len(d)
                d[c] = code
            return code

        for a, b in zip(s, t):
            a_code = get_code(a, s_dict)
            b_code = get_code(b, t_dict)

            if a_code != b_code:
                return False

        return True


def test(testObj: unittest.TestCase, s: str, t: str, expected: bool) -> None:
    so = Solution()
    actual = so.isIsomorphic(s, t)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "egg",  "add", True)

    def test_2(self):
        test(self,   "foo",  "bar", False)

    def test_3(self):
        test(self,   "paper",  "title", True)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
59 ms
Beats
75.7%
'''
