import unittest


class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self._index: dict[str, int] = {name: 0 for name in names}
        self._tables: dict[str, dict[int, list[str]]] = {name: {} for name in names}

    def insertRow(self, name: str, row: list[str]) -> None:
        table = self._tables[name]
        self._index[name] += 1
        table[self._index[name]] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self._tables[name]
        del table[rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self._tables[name]
        row = table[rowId]
        return row[columnId - 1]


def test(testObj: unittest.TestCase, actions: list, params: list, expected: list) -> None:
    n = len(actions)
    obj = SQL(*params[0])
    print("------------test case-----------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print("-------done-------------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insertRow":
                obj.insertRow(*params[i])
            case "deleteRow":
                obj.deleteRow(*params[i])
            case "selectCell":
                selectCell_actual = obj.selectCell(*params[i])
                testObj.assertEqual(selectCell_actual, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            ["SQL", "insertRow", "selectCell", "insertRow", "deleteRow", "selectCell"],
            [
                [["one", "two", "three"], [2, 3, 1]],
                ["two", ["first", "second", "third"]],
                ["two", 1, 3],
                ["two", ["fourth", "fifth", "sixth"]],
                ["two", 1],
                ["two", 2, 2],
            ],
            [None, None, "third", None, None, "fifth"],
        )


if __name__ == "__main__":
    unittest.main()


"""
Runtime
474 ms
Beats
92.98%
"""
