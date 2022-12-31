import unittest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            # if k == 0:
            #     break
            if stack or c != '0':
                stack.append(c)

        if k:
            stack = stack[:-k]

        ans = ''.join(stack)
        if ans == '':
            ans = '0'

        return ans


def test(testObj: unittest.TestCase, num: str, k: int, expected: int) -> None:

    so = Solution()
    actual = so.removeKdigits(num, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "1432219",  3, "1219")

    def test_2(self):
        test(self,   "10200",  1, "200")

    def test_3(self):
        test(self,   "10",  2, "0")

    def test_4(self):
        test(self,   "100",  2, "0")

    def test_5(self):
        test(self,   "12345",  1, "1234")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 69 ms, faster than 95.38%
Memory Usage: 15.5 MB, less than 42.47%
'''
