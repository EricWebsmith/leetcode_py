import unittest


class Solution:
    def findRLEArray(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
        ans: list = []
        v_prev, c_prev = -1, -1
        while len(encoded1) > 0:
            v1, c1 = encoded1.pop()
            v2, c2 = encoded2.pop()
            v = v1 * v2
            c = min(c1, c2)

            if c1-c > 0:
                encoded1.append([v1, c1-c])
            if c2-c > 0:
                encoded2.append([v2, c2-c])

            if len(ans) > 0:
                v_prev, c_prev = ans[-1]

            if v_prev == v:
                ans[-1] = [v, c+c_prev]
            else:
                ans.append([v1 * v2, c])

        ans.reverse()
        return ans


def test(testObj: unittest.TestCase, encoded1: list[list[int]], encoded2: list[list[int]], expected: int) -> None:

    so = Solution()
    actual = so.findRLEArray(encoded1, encoded2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 3], [2, 3]],  [[6, 3], [3, 3]], [[6, 6]])

    def test_2(self):
        test(self,   [[1, 3], [2, 1], [3, 2]],  [
             [2, 3], [3, 3]], [[2, 3], [6, 1], [9, 2]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 2828 ms, faster than 96.16%
Memory Usage: 67.3 MB, less than 96.91%
'''
