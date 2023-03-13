import unittest


class Solution:

    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels ='aeiou'            
        ans = 0
        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                ans += 1

        return ans


def test(testObj: unittest.TestCase, words: list[str], left: int, right: int, expected: int) -> None:
    so = Solution()
    actual = so.vowelStrings(words, left, right)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   ["are","amy","u"],  0,  2, 2)

    def test_2(self):
        test(self,   ["hey","aeo","mu","ooo","artro"],  1,  4, 3)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
75 ms
Beats
100%
'''
