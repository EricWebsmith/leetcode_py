import unittest


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        arr: list = []
        i = sequence.find(word)

        while i > -1:
            arr.append(i)
            i = sequence.find(word, i+1)

        s = dict()
        for i in arr:
            if i-len(word) in s:
                s[i] = s[i-len(word)] + 1
            else:
                s[i] = 1

        ans = 0
        for _, v in s.items():
            ans = max(ans, v)

        return ans


def test(testObj: unittest.TestCase, sequence: str, word: str, expected: int) -> None:
    so = Solution()
    actual = so.maxRepeating(sequence, word)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "ababc",  "ab", 2)

    def test_2(self):
        test(self,   "ababc",  "ba", 1)

    def test_3(self):
        test(self,   "ababc",  "ac", 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
36 ms
Beats
88.99%
'''
