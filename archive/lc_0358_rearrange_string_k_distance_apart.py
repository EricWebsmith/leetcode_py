import unittest
from typing import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s)
        most_common = counts.most_common()
        first_count = most_common[0][1]
        min_length = (first_count - 1) * k + 1
        ties = 1
        while ties < len(most_common) and most_common[ties][1] == first_count:
            min_length += 1
            ties += 1

        if min_length > len(s):
            return ""

        head = most_common[0][0]
        for i in range(1, ties):
            head += most_common[i][0]

        def generate_chars():
            for i in range(ties, len(most_common)):
                for _ in range(most_common[i][1]):
                    yield most_common[i][0]

        g = generate_chars()

        subs = [head] * (first_count - 1)
        while subs:
            try:
                for i in range(len(subs)):
                    subs[i] += next(g)
            except StopIteration:
                break

        subs.append(head)
        return "".join(subs)


def test(testObj: unittest.TestCase, s: str, k: int, expected: str) -> None:

    so = Solution()

    actual = so.rearrangeString(s, k)
    print(actual)
    testObj.assertTrue(actual in expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "aabbcc", 3, ["abcabc"])

    def test_2(self):
        test(self, "aaabc", 3, [""])

    def test_3(self):
        test(self, "aaadbbcc", 2, ["abcdabca", "abacabcd", "abacdabc"])

    def test_4(self):
        test(self, "a", 0, ["a"])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 90 ms, faster than 88.54%
Memory Usage: 15 MB, less than 86.76%
"""
