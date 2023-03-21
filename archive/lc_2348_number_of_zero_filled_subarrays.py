import unittest


def arithmetic_series_sum(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers using the arithmetic series formula.
    
    Args:
        n (int): The number of terms to sum.
    
    Returns:
        int: The sum of the first n natural numbers.
    """
    return (1 + n) * n // 2


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Find the total number of zero-filled subarrays in the input list.
        
        Args:
            nums (list[int]): A list of integers.
        
        Returns:
            int: The total number of zero-filled subarrays in the input list.
        """
        # Append 1 to the input list nums to ensure that the last zero-filled subarray is counted
        nums.append(1)
        
        # Initialize the counter for the consecutive zeros (n) and the total number of zero-filled subarrays (ans)
        n = 0
        ans = 0
        
        # Iterate through the nums list
        for num in nums:
            # If the current number is 0, increment the counter n
            if num == 0:
                n += 1
            else:
                # If the current number is not 0, add the number of zero-filled subarrays found
                # so far to the ans variable using the arithmetic_series_sum function
                ans += arithmetic_series_sum(n)
                
                # Reset the counter for consecutive zeros (n) to 0
                n = 0

        # Return the total number of zero-filled subarrays found
        return ans


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.zeroFilledSubarray(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 3, 0, 0, 2, 0, 0, 4], 6)

    def test_2(self):
        test(self, [0, 0, 0, 2, 0, 0], 9)

    def test_3(self):
        test(self, [2, 10, 2019], 0)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
1064 ms
Beats
87.99%
"""
