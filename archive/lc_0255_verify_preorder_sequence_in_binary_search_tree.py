import unittest


class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        check = None
        stack: list[int] = []
        for n in preorder:
            while stack and n > stack[-1]:
                check = stack.pop()
            if check is not None and n < check:
                return False
            stack.append(n)
        return True


def test(testObj: unittest.TestCase, preorder: list[int], expected: int) -> None:

    so = Solution()
    actual = so.verifyPreorder(preorder)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [5, 2, 1, 3, 6], True)

    def test_2(self):
        test(self, [5, 2, 6, 1, 3], False)

    def test_3(self):
        test(self, [3, 1, 2], True)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 239 ms, faster than 88.43%
Memory Usage: 14.9 MB, less than 66.44%
"""
