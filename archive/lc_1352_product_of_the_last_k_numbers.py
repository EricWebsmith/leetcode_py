import unittest
from typing import List


class ProductOfNumbers:
    def __init__(self) -> None:
        self.preprod: List[int] = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.preprod = [1]
        else:
            self.preprod.append(self.preprod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.preprod):
            return 0
        return self.preprod[-1] // self.preprod[-k - 1]


def test(
    testObj: unittest.TestCase, actions: List, params: List, expected: List
) -> None:
    n = len(actions)
    obj = ProductOfNumbers(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "add":
                obj.add(*params[i])

            case "getProduct":
                actual = obj.getProduct(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                "ProductOfNumbers",
                "add",
                "add",
                "add",
                "add",
                "add",
                "getProduct",
                "getProduct",
                "getProduct",
                "add",
                "getProduct",
            ],
            [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
            [None, None, None, None, None, None, 20, 40, 0, None, 32],
        )


if __name__ == "__main__":
    unittest.main()

# k will not be invalid
# 'getProduct' arguments are invalid: expected 'k' to have value from 1 to 6 only


"""
Runtime: 379 ms, faster than 64.05%
Memory Usage: 28.9 MB, less than 49.78%
"""
