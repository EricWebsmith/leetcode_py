import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode



class Solution:
    def __init__(self) -> None:
        self.stack: list = []

    def deal_mul_div(self):
        stack = self.stack
        if len(stack) >= 3 and type(stack[-3]) is TreeNode and type(stack[-1]) is TreeNode and stack[-2] in ["*", "/"]:
            t = TreeNode(stack[-2])
            t.left = stack[-3]
            t.right = stack[-1]
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(t)

    def expTree(self, s: str) -> TreeNode:
        stack = self.stack
        current = ""
        op = ""
        for c in s + "+":
            if c in "0123456789":
                current += c
            else:
                op = c
                if current != "":
                    stack.append(TreeNode(current))
                current = ""
                self.deal_mul_div()

                if op in "+-)":
                    head_node: Optional[TreeNode] = None
                    current_node: Optional[TreeNode] = None

                    while len(self.stack) >= 2 and type(stack[-1]) is TreeNode and stack[-2] in ["+", "-"]:

                        t = TreeNode(stack[-2])
                        t.right = stack[-1]

                        if head_node is None:
                            head_node = t
                            current_node = t
                        else:
                            current_node.left = t  # type: ignore
                            current_node = t
                        stack.pop()
                        stack.pop()

                    if head_node:
                        first = stack.pop()
                        current_node.left = first  # type: ignore
                        stack.append(head_node)

                if op == ")":
                    t = stack.pop()
                    # pop '('
                    stack.pop()
                    stack.append(t)
                    self.deal_mul_div()
                    continue
                else:
                    stack.append(op)

        return stack[0]


def test(testObj: unittest.TestCase, s: str, expected: List[str]) -> None:

    so = Solution()

    actual_root = so.expTree(s)
    actual = TreeNode.to_array(actual_root)
    print(actual)
    print(expected)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "3*4-2*5", ["-", "*", "*", "3", "4", "2", "5"])

    def test_2(self):
        test(
            self,
            "2-3/(5*2)+1",
            [
                "+",
                "-",
                "1",
                "2",
                "/",
                None,
                None,
                None,
                None,
                "3",
                "*",
                None,
                None,
                "5",
                "2",
            ],
        )

    def test_3(self):
        test(
            self,
            "1+2+3+4+5",
            ["+", "+", "5", "+", "4", None, None, "+", "3", None, None, "1", "2"],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 42 ms, faster than 72.01%,
Memory Usage: 14.2 MB, less than 30.63%
"""
