import unittest
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        s1 = s2 = 0
        n1, n2 = len(slots1), len(slots2)

        while s1 < n1 and s2 < n2:
            end = min(slots1[s1][1], slots2[s2][1])
            start = max(slots1[s1][0], slots2[s2][0])

            if end - start >= duration:
                return [start, start + duration]

            if slots2[s2][1] < slots1[s1][1]:
                s2 += 1
            elif slots2[s2][1] > slots1[s1][1]:
                s1 += 1
            else:
                # fallback if both end times are equal, could also be s1
                s1 += 1
                s2 += 1

        return []


def checkList(list1: List[int], list2: List[int]) -> bool:
    if len(list1) != len(list2):
        return False

    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def test(
    testObj: unittest.TestCase,
    slots1: List[List[int]],
    slots2: List[List[int]],
    duration: int,
    expected: List[int],
) -> None:
    s = Solution()
    actual = s.minAvailableDuration(slots1, slots2, duration)
    same = checkList(actual, expected)
    testObj.assertTrue(same)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8, [60, 68])

    def test_2(self):
        test(self, [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12, [])


if __name__ == "__main__":
    unittest.main()

# Runtime: 592 ms, faster than 90.15%
# Memory Usage: 21.5 MB, less than 72.61%
