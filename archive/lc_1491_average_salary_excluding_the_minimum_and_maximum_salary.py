import unittest


class Solution:
    def average(self, salary: list[int]) -> float:
        min_value = salary[0]
        max_value = salary[0]
        sum_value = 0
        for s in salary:
            min_value = min(min_value, s)
            max_value = max(max_value, s)
            sum_value += s

        sum_value = sum_value - min_value - max_value
        return sum_value / (len(salary) - 2)


def test(testObj: unittest.TestCase, salary: list[int], expected: float) -> None:
    so = Solution()
    actual = so.average(salary)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [4000,3000,1000,2000], 2500.00000)

    def test_2(self):
        test(self,   [1000,2000,3000], 2000.00000)


if __name__ == '__main__':
    unittest.main()


'''

'''
