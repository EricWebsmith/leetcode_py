from bisect import bisect_left, insort_left
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Leaderboard:

    def __init__(self):
        self.player_score_dict = defaultdict(int)
        self.score_player: List[List[int]] = []
        self.n = 0
    
    def find_player_by_score(self, score: int, playerId: int):
        index = bisect_left(self.score_player, x=score, key=lambda x: x[0])
        while index+1<self.n and self.score_player[index][0] == score and self.score_player[index][1] != playerId:
            index+=1
        return index


    def addScore(self, playerId: int, score: int) -> None:
        if not playerId in self.player_score_dict:
            self.player_score_dict[playerId] = score
            self.n+=1
            new_index = bisect_left(self.score_player, x=score,  key=lambda x: x[0])
            self.score_player.insert(new_index, [score, playerId])
        else:
            old_score = self.player_score_dict[playerId]
            new_score = old_score + score
            index = self.find_player_by_score(old_score, playerId)
            self.score_player =  self.score_player[:index] + self.score_player[index+1:]
            new_index = bisect_left(self.score_player, x=new_score,  key=lambda x: x[0])
            self.score_player.insert(new_index, [new_score, playerId])
            self.player_score_dict[playerId] = new_score


    def top(self, k: int) -> int:
        ans = 0
        for i in range(self.n-k,self.n,1):
            ans += self.score_player[i][0]
        return ans

    def reset(self, playerId: int) -> None:
        old_score = self.player_score_dict[playerId]
        index = self.find_player_by_score(old_score, playerId)
        
        if index<len(self.score_player) and self.score_player[index][1] == playerId:
            self.score_player =  self.score_player[:index] + self.score_player[index+1:]

        del self.player_score_dict[playerId]
        self.n-=1


def test(testObj: unittest.TestCase, actions:List, params:List , expected:List) -> None:
    n = len(actions)
    obj = Leaderboard(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            

            case "addScore":
                actual = obj.addScore(*params[i])
                testObj.assertEqual(actual, expected[i])
            
            case "top":
                actual = obj.top(*params[i])
                testObj.assertEqual(actual, expected[i])
            
            case "reset":
                actual = obj.reset(*params[i])
                testObj.assertEqual(actual, expected[i])
            
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self, ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"], [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]], [None,None,None,None,None,None,73,None,None,None,141])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 65 ms, faster than 95.95% of Python3 online submissions for Design A Leaderboard.
Memory Usage: 14.4 MB, less than 38.09% of Python3 online submissions for Design A Leaderboard.
'''
