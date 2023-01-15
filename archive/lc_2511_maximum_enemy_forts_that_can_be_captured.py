import unittest


class Solution:
    def captureForts(self, forts: list[int]) -> int:
        n = len(forts)
        zeros = 0
        before_zero = 0
        ans = 0
        for i in range(n):
            if forts[i] == 0:
                zeros += 1
            elif forts[i] == 1:
                if before_zero == -1:
                    ans = max(ans, zeros)
                zeros = 0
                before_zero = 1
            else:  # -1
                if before_zero == 1:
                    ans = max(ans, zeros)
                zeros = 0
                before_zero = -1

        return ans


def test(testObj: unittest.TestCase, forts: list[int], expected: int) -> None:
    so = Solution()
    actual = so.captureForts(forts)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 0, 0, -1, 0, 0, 0, 0, 1], 4)

    def test_2(self):
        test(self,   [0, 0, 1, -1], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
29 ms
Beats
98.49%
'''
