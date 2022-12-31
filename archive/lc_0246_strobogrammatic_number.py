import unittest


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        if n == 1 and num != '8' and num != '1' and num != '0':
            return False

        left = 0
        right = n-1
        while left < right:
            if num[left] == '9' and num[right] == '6' \
                    or num[left] == '6' and num[right] == '9' \
                    or num[left] == '8' and num[right] == '8' \
                    or num[left] == '1' and num[right] == '1' \
                    or num[left] == '0' and num[right] == '0':
                left += 1
                right -= 1
            else:
                return False

        if left == right:
            return num[left] == '1' or num[left] == '8' or num[left] == '0'

        return True


def test(testObj: unittest.TestCase, num: str, expected: bool) -> None:
    so = Solution()
    actual = so.isStrobogrammatic(num)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "69", True)

    def test_2(self):
        test(self,   "88", True)

    def test_3(self):
        test(self,   "962", False)

    def test_4(self):
        test(self,   "2", False)

    def test_5(self):
        test(self,   "1", True)

    def test_6(self):
        test(self,   "659", False)

    def test_7(self):
        test(self,   "101", True)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
33 ms
Beats
88.91%
'''
