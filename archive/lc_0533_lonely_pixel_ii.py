import unittest
from typing import Counter, List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m = len(picture)
        n = len(picture[0])

        rows = [0] * m
        cols = [0] * n
        rows_signatures = []
        for r in range(m):
            signature = 0
            for c in range(n):
                if picture[r][c] == 'B':
                    rows[r] += 1
                    cols[c] += 1
                    signature += (1 << c)
            rows_signatures.append(signature)

        ctr = Counter(rows_signatures)

        ans = 0
        for r in range(m):
            if ctr[rows_signatures[r]] != target:
                continue

            for c in range(n):
                if picture[r][c] == 'B' and rows[r] == target and cols[c] == target:
                    ans += 1

        return ans


def test(testObj: unittest.TestCase, picture: List[List[str]], target: int, expected: int) -> None:

    so = Solution()

    actual = so.findBlackPixel(picture, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [["W", "B", "W", "B", "B", "W"], ["W", "B", "W", "B", "B", "W"],
             ["W", "B", "W", "B", "B", "W"], ["W", "W", "B", "W", "B", "W"]],  3, 6)

    def test_2(self):
        test(self,   [["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]],  1, 0)

    def test_3(self):
        test(self,   [["W", "B", "W", "B", "B", "W"], ["B", "W", "B", "W", "W", "B"], ["W", "B", "W", "B", "B", "W"], [
             "B", "W", "B", "W", "W", "B"], ["W", "W", "W", "B", "B", "W"], ["B", "W", "B", "W", "W", "B"]],  3, 9)


if __name__ == '__main__':
    unittest.main()

'''
Here rule two means we need `target-1` rows that are same as row `r`.
So if there are exactly `target` rows share the same signature, those rows are valid.
And here is the magic, in python there is no limit in interger!!!
So we can use bit mask!!!

Try this:

for i in range(200):
    print(1<<i)


Performance:
565ms, 96.15%
'''
