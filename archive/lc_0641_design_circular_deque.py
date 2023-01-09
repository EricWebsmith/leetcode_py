import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.pre: Node | None = None
        self.next: Node | None = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.first: Node | None = None
        self.last: Node | None = None
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False
        if self.size == 0:
            self.first = Node(value)
            self.last = self.first
        else:
            new_first = Node(value)
            # double link
            new_first.next = self.first
            assert self.first is not None
            self.first.pre = new_first
            self.first = new_first
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False

        if self.size == 0:
            self.first = Node(value)
            self.last = self.first
        else:
            new_last = Node(value)
            # double link
            new_last.pre = self.last
            assert self.last is not None
            self.last.next = new_last
            self.last = new_last

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        if self.size == 1:
            self.first = None
            self.last = None
            self.size = 0
            return True

        assert self.first is not None
        new_front = self.first.next
        assert new_front is not None
        new_front.pre = None
        self.first = new_front

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.first = None
            self.last = None
            self.size = 0
            return True

        assert self.last is not None
        new_last = self.last.pre
        assert new_last is not None
        new_last.next = None
        self.last = new_last
        self.size -= 1

        return True

    def getFront(self) -> int:
        if self.first:
            return self.first.val
        return -1

    def getRear(self) -> int:
        if self.last:
            return self.last.val
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


def test(testObj: unittest.TestCase, actions: list, params: list, expected: list) -> None:
    n = len(actions)
    print(0, '__init__', params[0])
    obj = MyCircularDeque(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insertFront":
                actual = obj.insertFront(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "insertLast":
                actual = obj.insertLast(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "deleteFront":
                actual = obj.deleteFront(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "deleteLast":
                actual = obj.deleteLast(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "getFront":
                actual_get_front = obj.getFront(*params[i])
                testObj.assertEqual(actual_get_front, expected[i])

            case "getRear":
                actual_get_rear = obj.getRear(*params[i])
                testObj.assertEqual(actual_get_rear, expected[i])

            case "isEmpty":
                actual = obj.isEmpty(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "isFull":
                actual = obj.isFull(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,
             ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
              "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
             [[3], [1], [2], [3], [4], [], [], [], [4], []],
             [None, True, True, True, False, 2, True, True, True, 4])

    def test_2(self):
        test(self,
             ["MyCircularDeque", "insertFront", "insertLast", "getFront", "insertLast",
              "getFront", "insertFront", "getRear", "getFront", "getFront", "deleteLast", "getRear"],
             [[5], [7], [0], [], [3], [], [9], [], [], [], [], []],
             [None, True, True, 7, True, 7, True, 3, 9, 9, True, 0])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 67 ms, faster than 98.39%
Memory Usage: 15.1 MB, less than 12.88%
'''
