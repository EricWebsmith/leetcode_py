import unittest


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output: list = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)


def test(testObj: unittest.TestCase, n: int, k: int, expected: str) -> None:

    so = Solution()
    actual = so.getPermutation(n, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3,  3, "213")

    def test_2(self):
        test(self,   4,  9, "2314")

    def test_3(self):
        test(self,   3,  1, "123")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 47 ms, faster than 68.92%
Memory Usage: 13.9 MB, less than 77.91%
'''
