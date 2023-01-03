import unittest


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        length = len(strs[0])
        columns_to_delete = 0
        for c in range(length):
            pre = strs[0][c]
            for i in range(1, n):
                cur = strs[i][c]
                if pre > cur:
                    columns_to_delete += 1
                    break
                pre = cur

        return columns_to_delete


def test(testObj: unittest.TestCase, strs: list[str], expected: int) -> None:
    so = Solution()
    actual = so.minDeletionSize(strs)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["cba", "daf", "ghi"], 1)

    def test_2(self):
        test(self,   ["a", "b"], 0)

    def test_3(self):
        test(self,   ["zyx", "wvu", "tsr"], 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
234 ms
Beats
59.79%
'''
