import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        num = 1
        for i in range(n-1):
            count = 1
            pre = num % 10
            num //= 10
            next_num = 0
            base = 1
            while num:
                cur = num % 10
                num //= 10
                if cur == pre:
                    count += 1
                else:
                    next_num += (count * 10 + pre) * base
                    base *= 100
                    pre = cur
                    count = 1
            next_num += (count * 10 + pre) * base
            num = next_num

        return str(num)


def test(testObj: unittest.TestCase, n: int, expected: str) -> None:
    so = Solution()
    actual = so.countAndSay(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1, "1")

    def test_4(self):
        test(self,   4, "1211")

    def test_10(self):
        test(self,   10, "13211311123113112211")

    def test_15(self):
        test(self,   15, "311311222113111231131112132112311321322112111312211312111322212311322113212221")

    def test_20(self):
        test(self,   20, "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211")  # noqa


if __name__ == '__main__':
    unittest.main()

'''

'''
