import unittest


def get_index(c: str) -> int:
    return ord(c) - ord('a')


def equal(counter1: list[int], counter2: list[int]) -> bool:
    for c1, c2 in zip(counter1, counter2):
        if c1 != c2:
            return False
    
    return True

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        
        counter_p = [0] * 26
        counter_s = [0] * 26
        for c in p:
            counter_p[get_index(c)] += 1

        for i in range(len(p)):
            counter_s[get_index(s[i])] += 1

        ans = []
        for i in range(len(p), len(s)):
            if equal(counter_p, counter_s):
                ans.append(i - len(p))
            counter_s[get_index(s[i])] += 1
            counter_s[get_index(s[i - len(p)])] -= 1
        
        if equal(counter_p, counter_s):
            ans.append(len(s)-len(p))
        
        return ans


def test(testObj: unittest.TestCase, s: str, p: str, expected:list[int]) -> None:
    so = Solution()
    actual = so.findAnagrams(s, p)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   "cbaebabacd",  "abc", [0,6])

    def test_2(self):
        test(self,   "abab",  "ab", [0,1,2])


    def test_3(self):
        test(self,   "aaaa",  "aa", [0,1,2])

if __name__ == '__main__':
    unittest.main()


'''
Runtime
182 ms
Beats
55.64%
'''
