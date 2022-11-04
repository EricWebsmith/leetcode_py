import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < n and not s[left] in vowels:
                left += 1

            while right > 0 and not s[right] in vowels:
                right -= 1

            if left >= right:
                break

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:

    so = Solution()
    actual = so.reverseVowels(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "hello", "holle")

    def test_2(self):
        test(self,   "leetcode", "leotcede")

    def test_3(self):
        test(self,   "aA", "Aa")


if __name__ == '__main__':
    unittest.main()

'''
Runtime
79 ms
Beats
81%
'''
