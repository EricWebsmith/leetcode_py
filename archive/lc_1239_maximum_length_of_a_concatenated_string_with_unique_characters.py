import unittest
from string import ascii_lowercase
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # masks from a to z, 2^0 to 2^25
        masks = {a: 1 << i for i, a in enumerate(ascii_lowercase)}

        nums: list = []
        for s in arr:
            num = 0
            skip = False
            for c in s:
                mask = masks[c]
                if num & mask == 0:
                    num |= mask
                else:
                    skip = True
                    break

            if skip:
                continue

            nums.append(num)

        def mask_to_length(mask: int) -> int:
            count = 0
            for i in range(26):
                if (1 << i) & mask > 0:
                    count += 1
            return count

        def dfs(i, mask_all):
            if i == len(nums):
                return mask_to_length(mask_all)

            res = 0
            if mask_all & nums[i] == 0:
                mask_all = mask_all | nums[i]
                res = dfs(i+1, mask_all)
                mask_all = mask_all - nums[i]

            return max(res, dfs(i+1, mask_all))

        return dfs(0, 0)


def test(testObj: unittest.TestCase, arr: List[str], expected: int) -> None:
    so = Solution()
    actual = so.maxLength(arr)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["un", "iq", "ue"], 4)

    def test_2(self):
        test(self,   ["cha", "r", "act", "ers"], 6)

    def test_3(self):
        test(self,   ["abcdefghijklmnopqrstuvwxyz"], 26)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
327 ms
Beats
30.27%
'''
