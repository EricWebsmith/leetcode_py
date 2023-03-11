import unittest


class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            r = num % 10
            digits.append(r)
            num //= 10

        digits.sort(reverse=True)

        s = 0
        for i in range(len(digits)):
            exponent = i // 2
            s += digits[i] * 10 ** exponent

        return s



def test(testObj: unittest.TestCase, num: int, expected: int) -> None:
    so = Solution()
    actual = so.splitNum(num)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   4325, 59)

    def test_2(self):
        test(self,   687, 75)


if __name__ == '__main__':
    unittest.main()


'''

'''
