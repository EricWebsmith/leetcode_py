import unittest


def get_index(c: str):
    return ord(c) - ord("a")


def count_equal(counter1: list[int], counter2: list[int]) -> bool:
    for c1, c2 in zip(counter1, counter2):
        if c1 != c2:
            return False

    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter1 = [0] * 26
        counter2 = [0] * 26

        for c in s1:
            index = get_index(c)
            counter1[index] += 1

        for i in range(len(s1)):
            index = get_index(s2[i])
            counter2[index] += 1

        for i in range(len(s1), len(s2)):
            if count_equal(counter1, counter2):
                return True
            index = get_index(s2[i])
            counter2[index] += 1
            pre_index = get_index(s2[i - len(s1)])
            counter2[pre_index] -= 1

        if count_equal(counter1, counter2):
            return True

        return False


def test(testObj: unittest.TestCase, s1: str, s2: str, expected: bool) -> None:
    so = Solution()
    actual = so.checkInclusion(s1, s2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "ab", "eidbaooo", True)

    def test_2(self):
        test(self, "ab", "eidboaoo", False)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
83 ms
Beats
67.4%
"""
