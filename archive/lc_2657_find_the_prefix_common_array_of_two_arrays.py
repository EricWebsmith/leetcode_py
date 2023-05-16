import unittest


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        setA = set[int]()
        setB = set[int]()
        ans = 0
        arr = []
        for i in range(len(A)):
            if A[i] in setB:
                ans += 1
                setB.remove(A[i])
            if B[i] in setA:
                ans += 1
                setA.remove(B[i])

            if A[i] == B[i]:
                ans += 1

            arr.append(ans)

            setA.add(A[i])
            setB.add(B[i])

        return arr


def test(testObj: unittest.TestCase, A: list[int], B: list[int], expected: list[int]) -> None:
    so = Solution()
    actual = so.findThePrefixCommonArray(A, B)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4])

    def test_2(self):
        test(self, [2, 3, 1], [3, 1, 2], [0, 1, 3])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
137 ms
Beats
83.33%
"""
