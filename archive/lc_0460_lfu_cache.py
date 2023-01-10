
import unittest


class LFUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.key_fre_dict: dict[int, int] = dict()
        self.fre_key_dict: dict[int, list[int]] = dict()
        self.key_value_dict: dict[int, int] = dict()

    def update_fre(self, key):

        fre = self.key_fre_dict[key]
        self.key_fre_dict[key] = fre + 1

        fre_list: list[int] = self.fre_key_dict[fre]
        fre_list.remove(key)
        if len(fre_list) == 0:
            del self.fre_key_dict[fre]

        if not (fre+1) in self.fre_key_dict:
            self.fre_key_dict[fre+1] = []
        self.fre_key_dict[fre+1].append(key)

    def free(self) -> None:
        min_fre = min(self.fre_key_dict.keys())
        key = self.fre_key_dict[min_fre][0]
        del self.fre_key_dict[min_fre][0]
        if len(self.fre_key_dict[min_fre]) == 0:
            del self.fre_key_dict[min_fre]

        del self.key_fre_dict[key]
        del self.key_value_dict[key]

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key not in self.key_value_dict:
            return -1

        self.update_fre(key)

        return self.key_value_dict[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.key_value_dict:
            if len(self.key_fre_dict) == self.capacity:
                self.free()
            self.key_value_dict[key] = value

            self.key_fre_dict[key] = 1
            if 1 not in self.fre_key_dict:
                self.fre_key_dict[1] = []
            self.fre_key_dict[1].append(key)
        elif key in self.key_value_dict:
            self.key_value_dict[key] = value
            self.update_fre(key)


def test(testObj: unittest.TestCase, actions: list, params: list, expected: list) -> None:
    n = len(actions)
    obj = LFUCache(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "get":
                actual = obj.get(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "put":
                obj.put(*params[i])


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"], [[2], [1, 1], [
             2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]], [None, None, None, 1, None, -1, 3, None, -1, 3, 4])


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 1203 ms, faster than 64.70%
Memory Usage: 78 MB, less than 71.79%
"""
