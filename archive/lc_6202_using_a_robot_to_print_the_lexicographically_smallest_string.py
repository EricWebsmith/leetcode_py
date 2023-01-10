import unittest


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        moving_min = s[n-1]
        right_min = [s[n-1]]
        for i in range(n-2, -1, -1):
            moving_min = min(moving_min, s[i])
            right_min.append(moving_min)
        right_min.reverse()

        paper = ''
        t: list = []
        for i in range(n):
            while t and t[-1] <= right_min[i]:
                paper += t.pop()

            t.append(s[i])

        t.reverse()
        return paper + ''.join(t)


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:
    so = Solution()
    actual = so.robotWithString(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "zza", "azz")

    def test_2(self):
        test(self,   "bac", "abc")

    def test_3(self):
        test(self,   "bdda", "addb")

    def test_4(self):
        test(self,   "bydizfve", "bdevfziy")

    def test_5(self):
        test(self,  "vzhofnpo", "fnohopzv")

    def test_6(self):
        test(self,  "adbecf", "abcedf")


if __name__ == '__main__':
    unittest.main()

'''
2434. Using a Robot to Print the Lexicographically Smallest String
'''
