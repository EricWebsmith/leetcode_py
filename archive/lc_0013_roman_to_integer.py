import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i_sign = 1
        x_sign = 1
        c_sign = 1
        for i in range(len(s)-1, -1, -1):
            match s[i]:
                case 'I':
                    ans += i_sign * 1
                case 'V':
                    ans += 5
                    i_sign = -1
                case 'X':
                    ans += x_sign * 10
                    i_sign = -1
                case 'L':
                    ans += 50
                    x_sign = -1
                case 'C':
                    ans += c_sign * 100
                    x_sign = -1
                case 'D':
                    ans += 500
                    c_sign = -1
                case 'M':
                    ans += 1000
                    c_sign = -1

        return ans


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:
    so = Solution()
    actual = so.romanToInt(s)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  "III", 3)

    def test_2(self):
        test(self,  "LVIII", 58)

    def test_3(self):
        test(self,  "MCMXCIV", 1994)


if __name__ == '__main__':
    unittest.main()
