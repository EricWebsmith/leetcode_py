import unittest
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        DNA_LENGTH = 8
        q = deque([(start, 0)])
        seen = {start}

        while q:
            node, steps = q.popleft()
            if node == end:
                return steps

            for c in "ATCG":
                for i in range(DNA_LENGTH):
                    neigbor = node[:i] + c + node[i + 1 :]
                    if neigbor not in seen and neigbor in bank:
                        q.append((neigbor, steps + 1))
                        seen.add(neigbor)

        return -1


def test(testObj: unittest.TestCase, start: str, end: str, bank: List[str], expected: int) -> None:

    so = Solution()
    actual = so.minMutation(start, end, bank)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1)

    def test_2(self):
        test(self, "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2)

    def test_3(self):
        test(self, "AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3)

    def test_4(self):
        test(self, "AACCGGTT", "AACCGGTA", [], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
37 ms
Beats
85.21%
"""
