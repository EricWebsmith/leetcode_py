
from collections import defaultdict
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Tuple
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.snaps = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        if index in self.snaps[index] and self.snaps[index][-1][0] == self.cur_snap_id:
            self.snaps[index][-1] = (self.cur_snap_id, val)
            return
        self.snaps[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id+=1
        return self.cur_snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.cur_snap_id:
            return 0
        
        arr = self.snaps[index]
        if len(arr) == 0:
            return 0

        if arr[0][0] > snap_id:
            return 0
        l = 0
        r = len(arr) - 1
        while l<r:
            m = (l + r + 1) >> 1
            if arr[m][0] <= snap_id:
                l = m 
            else:
                r = m - 1
        
        return self.snaps[index][l][1]


def test(testObj: unittest.TestCase, actions:List, params:List , expected:List) -> None:
    n = len(actions)
    obj = SnapshotArray(params[0][0])
    for i in range(1, n):
        match actions[i]:
            case "set":
                actual = obj.set(*params[i])
                testObj.assertEqual(actual, expected[i])
            
            case "snap":
                actual = obj.snap(*params[i])
                testObj.assertEqual(actual, expected[i])
            
            case "get":
                actual = obj.get(*params[i])
                testObj.assertEqual(actual, expected[i])
            
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self, ["SnapshotArray","set","snap","set","get"], [[3],[0,5],[],[0,6],[0,0]], [None,None,0,None,5])
    
    def test_2(self):
        test(self, ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"],
            [[1],[0,15],[],[],[],[0,2],[],[],[0,0]],
            [None,None,0,1,2,15,3,4,15]
        )
    

if __name__ == '__main__':
    unittest.main()
        