import sys
import unittest
from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]) -> None:
        self.locations = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        best = sys.maxsize
        p1 = 0
        p2 = 0
        while p1 < len(loc1) and p2 < len(loc2):
            if loc1[p1] > loc2[p2]:
                best = min(best, loc1[p1] - loc2[p2])
                p2 += 1
            else:
                best = min(best, loc2[p2] - loc1[p1])
                p1 += 1

        return best


def test(
    testObj: unittest.TestCase, actions: List, params: List, expected: List
) -> None:
    n = len(actions)
    obj = WordDistance(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "shortest":
                actual = obj.shortest(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            ["WordDistance", "shortest", "shortest"],
            [
                [["practice", "makes", "perfect", "coding", "makes"]],
                ["coding", "practice"],
                ["makes", "coding"],
            ],
            [None, 3, 1],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 106 ms, faster than 90.05%
Memory Usage: 22 MB, less than 9.35%
"""
