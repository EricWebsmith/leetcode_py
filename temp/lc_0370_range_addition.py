import unittest


class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        ans = [0] * length
        for update in updates:
            ans[update[0]] += update[2]
            if update[1] + 1 < length:
                ans[update[1]+1] -= update[2]

        prev = 0
        for i in range(length):
            ans[i] += prev
            prev = ans[i]

        return ans


def test(testObj: unittest.TestCase, length: int, updates: list[list[int]], expected: list[int]) -> None:
    so = Solution()
    actual = so.getModifiedArray(length, updates)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   5,  [[1, 3, 2], [2, 4, 3], [0, 2, -2]], [-2, 0, 3, 5, 3])

    def test_2(self):
        test(self,   10,  [[2, 4, 6], [5, 6, 8], [1, 9, -4]], [0, -4, 2, 2, 2, 4, 4, -4, -4, -4])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
168 ms
Beats
95.32%
'''
