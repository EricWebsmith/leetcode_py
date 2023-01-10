import unittest
from typing import List


class Solution:
    def __init__(self) -> None:
        self.operations = '+-*'
        self.cache: dict = dict()

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.cache:
            return self.cache[expression]

        n = len(expression)
        if n <= 2:
            return [int(expression)]

        if n <= 3 and expression[0] == '-':
            return [int(expression)]

        results: list = []
        for i in range(1, n):
            if expression[i] in self.operations:
                left_parts = self.diffWaysToCompute(expression[:i])
                right_parts = self.diffWaysToCompute(expression[i+1:])
                for left_part in left_parts:
                    for right_part in right_parts:
                        match expression[i]:
                            case '+':
                                results.append(left_part+right_part)
                            case '-':
                                results.append(left_part-right_part)
                            case '*':
                                results.append(left_part*right_part)

        # comment out when submitting to leetcode
        results.sort()
        self.cache[expression] = results
        return results


def test(testObj: unittest.TestCase, expression: str, expected: int) -> None:

    so = Solution()
    actual = so.diffWaysToCompute(expression)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "2-1-1", [0, 2])

    def test_2(self):
        test(self,   "2*3-4*5", [-34, -14, -10, -10, 10])

    def test_3(self):
        test(self,   "-2-1-1", [-4, -2])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 39 ms, faster than 87.98%
Memory Usage: 13.9 MB, less than 85.54%
'''
