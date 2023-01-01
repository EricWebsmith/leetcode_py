import unittest


class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        distance = 1_000_000
        for i, word in enumerate(words):
            if word != target:
                continue
            distance = min(distance, (startIndex - (i - n)))
            distance = min(distance, abs(startIndex - i))
            distance = min(distance, ((i + n) - startIndex))

        if distance == 1_000_000:
            distance = -1

        return distance


def test(testObj: unittest.TestCase, words: list[str], target: str, startIndex: int, expected: int) -> None:
    so = Solution()
    actual = so.closetTarget(words, target, startIndex)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["hello", "i", "am", "leetcode", "hello"],  "hello",  1, 1)

    def test_2(self):
        test(self,   ["a", "b", "leetcode"],  "leetcode",  0, 1)

    def test_3(self):
        test(self,   ["i", "eat", "leetcode"],  "ate",  0, -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
51 ms
Beats
80.92%
'''
