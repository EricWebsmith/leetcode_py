import unittest


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n_missing = 0
        current = 0
        arr_index = 0
        while True:
            current += 1
            if arr_index < len(arr) and current == arr[arr_index]:
                arr_index += 1
            else:
                n_missing += 1
                if n_missing == k:
                    return current


        return -1


def test(testObj: unittest.TestCase, arr: list[int], k: int, expected:int) -> None:
    so = Solution()
    actual = so.findKthPositive(arr, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [2,3,4,7,11],  5, 9)

    def test_2(self):
        test(self,   [1,2,3,4],  2, 6)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
49 ms
Beats
86.17%
'''
