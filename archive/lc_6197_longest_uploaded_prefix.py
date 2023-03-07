import unittest
from typing import List

null = None


class LUPrefix:
    def __init__(self, n: int) -> None:
        self.n = n
        self.arr = [-1] * n
        self.last = -1

    def upload(self, video: int) -> None:
        self.arr[video - 1] = 1
        new_index = self.last
        while new_index < self.n - 1 and self.arr[new_index + 1] == 1:
            new_index += 1

        self.last = new_index

    def longest(self) -> int:
        return self.last + 1


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = LUPrefix(*params[0])
    print("------------test case-----------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print("-------done-------------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "upload":
                actual = obj.upload(*params[i])  # type: ignore
                testObj.assertEqual(actual, expected[i])

            case "longest":
                actual = obj.longest(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"],
            [[4], [3], [], [1], [], [2], []],
            [None, None, 0, None, 1, None, 3],
        )

    def test_2(self):
        test(
            self,
            [
                "LUPrefix",
                "upload",
                "longest",
                "upload",
                "longest",
                "upload",
                "longest",
                "upload",
                "longest",
            ],
            [[4], [3], [], [1], [], [2], [], [4], []],
            [None, None, 0, None, 1, None, 3, None, 4],
        )


if __name__ == "__main__":
    unittest.main()
