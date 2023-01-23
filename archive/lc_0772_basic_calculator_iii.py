import unittest
from typing import List, Optional


class Solution:
    def __init__(self) -> None:
        self.stack: List[(int | str)] = []
        self.op = ""
        self.current: Optional[int] = None

    def calc_multiply_divide(self):
        stack = self.stack
        if len(stack) >= 3 and type(stack[-1]) is int and type(stack[-3]) is int and stack[-2] in ["*", "/"]:
            if stack[-2] == "*":
                t = stack[-3] * stack[-1]
            elif stack[-2] == "/":
                sign = 1
                if stack[-3] < 0:
                    sign = -sign
                    stack[-3] = -stack[-3]
                if stack[-1] < 0:
                    sign = -sign
                    stack[-1] = -stack[-1]

                t = stack[-3] // stack[-1] * sign

            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(t)

    def calculate(self, s: str) -> int:
        stack = self.stack
        for c in s + "+":
            if "0" <= c <= "9":
                self.current = self.current or 0
                t = int(c)
                self.current = self.current * 10 + t
            elif c in "+-*/()":
                if self.current is not None:
                    self.stack.append(self.current)

                new_op = c

                self.current = None

                # * and / first
                self.calc_multiply_divide()

                if new_op in "+-)":
                    t = 0
                    while len(self.stack) >= 2 and type(stack[-1]) is int and stack[-2] in ["+", "-"]:
                        if stack[-2] == "+":
                            t += stack[-1]
                        else:
                            t -= stack[-1]
                        stack.pop()
                        stack.pop()

                    first = stack.pop()
                    t = int(first) + t
                    stack.append(t)

                if new_op == ")":
                    t = int(stack.pop())
                    stack.pop()
                    stack.append(t)
                    self.calc_multiply_divide()
                    continue
                else:
                    stack.append(new_op)

        return int(stack[0])


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.calculate(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "3+2*2", 7)

    def test_2(self):
        test(self, " 3/2 ", 1)

    def test_3(self):
        test(self, " 3+5 / 2 ", 5)

    def test_4(self):
        test(self, "14-3/2", 13)

    def test_5(self):
        test(self, "1+1", 2)

    def test_6(self):
        test(self, "6-4/2", 4)

    def test_7(self):
        test(self, "2*(5+5*2)/3+(6/2+8)", 21)

    def test_8(self):
        test(self, "2*(5+5*2)", eval("2*(5+5*2)"))

    def test_9(self):
        test(self, "(2+6*3+5-(3*14/7+2)*5)+3", -12)

    def test_10(self):
        test(self, "(0-3)/4", 0)

    def test_11(self):
        test(self, "3/(2/1-4)", -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 55 ms, faster than 70.33%
Memory Usage: 13.8 MB, less than 94.41%
"""
