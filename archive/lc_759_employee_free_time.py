from heapq import heapify, heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        
        hq = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                hq.append([schedule[i][j].start, schedule[i][j].end])
        
        hq.sort()
        
        prev_end = -1
        ans = []
        while len(hq)>0:
            first = hq.pop(0)
            if first[0] > prev_end:
                ans.append(Interval(prev_end, first[0]))

            prev_end = max(prev_end, first[1]) 
        
        return ans[1:]


def test(testObj: unittest.TestCase, schedule_arr: '[[Interval]]', expected:int) -> None:
    schedule = []
    for i in range(len(schedule_arr)):
        person = []
        for j in range(len(schedule_arr[i])):
            person.append(Interval(*schedule_arr[i][j]))
        schedule.append(person)
    so = Solution()
    actual_arr = so.employeeFreeTime(schedule)
    actual = []
    for i in range(len(actual_arr)):
        actual.append([actual_arr[i].start, actual_arr[i].end])
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [[[1,2],[5,6]],[[1,3]],[[4,10]]], [[3,4]])

    def test_2(self):
        test(self,   [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]], [[5,6],[7,9]])
    
    def test_3(self):
        test(self,   
            [[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]],
            [[26,27],[36,39],[87,91]])
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 95 ms, faster than 91.67% of Python3 online submissions for Employee Free Time.
Memory Usage: 15.7 MB, less than 78.36% of Python3 online submissions for Employee Free Time.
'''
