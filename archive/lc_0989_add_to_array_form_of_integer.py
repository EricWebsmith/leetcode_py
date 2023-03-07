import unittest


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        carry = 0
        # bear in mind that index is alway negative.
        index = -1
        while k > 0 or carry == 1:
            # insert 0 to index, if num[index] does not exist.
            if -index > len(num):
                num.insert(0, 0)
            k_digit = k % 10
            k = k // 10
            s = k_digit + num[index] + carry
            carry = s // 10
            num[index] = s % 10

            index -= 1

        return num


def test(testObj: unittest.TestCase, num: list[int], k: int, expected: list[int]) -> None:
    so = Solution()
    actual = so.addToArrayForm(num, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 0, 0], 34, [1, 2, 3, 4])

    def test_2(self):
        test(self, [2, 7, 4], 181, [4, 5, 5])

    def test_3(self):
        test(self, [2, 1, 5], 806, [1, 0, 2, 1])

    def test_4(self):
        test(self, [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
276 ms
Beats
89.91%
"""
