import unittest
from collections import defaultdict
from typing import List


class HitCounter:

    def __init__(self) -> None:
        self.hits: dict = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        keys = list(self.hits.keys())
        for k in keys:
            if k <= timestamp-300:
                del self.hits[k]

        return sum(self.hits.values())


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = HitCounter(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "hit":
                obj.hit(*params[i])

            case "getHits":
                actual = obj.getHits(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"], [
             [], [1], [2], [3], [4], [300], [300], [301]], [None, None, None, None, 3, None, 4, 3])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 35 ms, faster than 88.20%
Memory Usage: 14 MB, less than 59.91%
'''
