import unittest
from collections import defaultdict
from typing import List

MOD = 1_000_000_007
BASE = 26


class Solution:
    def search(self, nums: List[int], w: int):
        """
        @param w: int window size
        @returns: int repeat substring index
        """
        n = len(nums)
        h = 0
        for i in range(w):
            h = (h * BASE + nums[i]) % MOD

        seen = defaultdict(list)
        seen[h].append(0)

        BASE_w = pow(BASE, w - 1, MOD)
        for i in range(1, n - w + 1):
            # pop out i-1
            h -= nums[i - 1] * BASE_w
            # push i+window-1
            h = (h * BASE + nums[i + w - 1]) % MOD
            if h in seen:
                current_substring = nums[i: i + w]
                if any(current_substring == nums[index: index + w] for index in seen[h]):
                    return i
            seen[h].append(i)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord("a") for c in s]
        start = -1
        left = 0
        right = n - 1

        while left < right:
            m = (left + right + 1) >> 1
            start_found = self.search(nums, m)

            if start_found != -1:
                start = start_found
                left = m
            else:
                right = m - 1

        return s[start: start + left]


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:

    so = Solution()

    actual = so.longestDupSubstring(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "banana", "ana")

    def test_2(self):
        test(self, "abcd", "")

    def test_3(self):
        test(
            self,
            "ababdaebdabedeabbdddbcebaccececbccccebbcaaabaadcadccddaedaacaeddddeceedeaabbbbcbacdaeeebaabdabdbaebadcbdebaaeddcadebedeabbbcbeadbaacdebceebceeccddbeacdcecbcdbceedaeebdaeeabccccbcccbceabedaedaacdbbdbadcdbdddddcdebbcdbcabbebbeabbdccccbaaccbbcecacaebebecdcdcecdeaccccccdbbdebaaaaaaeaaeecdecedcbabedbabdedbaebeedcecebabedbceecacbdecabcebdcbecedccaeaaadbababdccedebeccecaddeabaebbeeccabeddedbeaadbcdceddceccecddbdbeeddabeddadaaaadbeedbeeeaaaeaadaebdacbdcaaabbacacccddbeaacebeeaabaadcabdbaadeaccaecbeaaabccddabbeacdecadebaecccbabeaceccaaeddedcaecddaacebcaecebebebadaceadcaccdeebbcdebcedaeaedacbeecceeebbdbdbaadeeecabdebbaaebdddeeddabcbaaebeabbbcaaeecddecbbbebecdbbbaecceeaabeeedcdecdcaeacabdcbcedcbbcaeeebaabdbaadcebbccbedbabeaddaecdbdbdccceeccaccbdcdadcccceebdabccaebcddaeeecddddacdbdbeebdabecdaeaadbadbebecbcacbbceeabbceecaabdcabebbcdecedbacbcccddcecccecbacddbeddbbbadcbdadbecceebddeacbeeabcdbbaabeabdbbbcaeeadddaeccbcdabceeabaacbeacdcbdceebeaebcceeebdcdcbeaaeeeadabbecdbadbebbecdceaeeecaaaedeceaddedbedbedbddbcbabeadddeccdaadaaeaeeadebbeabcabbdebabeedeeeccadcddaebbedadcdaebabbecedebadbdeacecdcaebcbdababcecaecbcbcdadacaebdedecaadbaaeeebcbeeedaaebbabbeeadadbacdedcbabdaabddccedbeacbecbcccdeaeeabcaeccdaaaddcdecadddabcaedccbdbbccecacbcdecbdcdcbabbeaacddaeeaabccebaaaebacebdcdcbbbdabadeebbdccabcacaacccccbadbdebecdaccabbecdabdbdaebeeadaeecbadedaebcaedeedcaacabaccbbdaccedaedddacbbbdbcaeedbcbecccdbdeddcdadacccdbcdccebdebeaeacecaaadccbbaaddbeebcbadceaebeccecabdadccddbbcbaebeaeadacaebcbbbdbcdaeadbcbdcedebabbaababaacedcbcbceaaabadbdcddadecdcebeeabaadceecaeccdeeabdbabebdcedceaeddaecedcdbccbbedbeecabaecdbba",  # noqa
            "aeeebaabd",
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1935 ms, faster than 89.79%
Memory Usage: 21.5 MB, less than 40.99%
"""
