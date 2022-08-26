from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt

from abc import ABC, abstractmethod 

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self) -> None:
        super().__init__()
        self.val = 0
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.opertion: str = ''

    def evaluate(self) -> int:
        return self.val

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operations = ['+', '-', '*', '/']
        stack = []
        for p in postfix:
            if not p in operations:
                node = TreeNode()
                node.val = int(p)
                stack.append(node)
            else:
                node = TreeNode()
                node.opertion = p
                node.right = stack.pop()
                node.left = stack.pop()
                
                match p:
                    case '+':
                        node.val = node.left.val + node.right.val
                    case '-':
                        node.val = node.left.val - node.right.val
                    case '*':
                        node.val = node.left.val * node.right.val
                    case '/':
                        node.val = node.left.val // node.right.val
                stack.append(node)

        return stack[0]


def test(testObj: unittest.TestCase, postfix:List[str], expected:int) -> None:
    obj = TreeBuilder()
    expTree = obj.buildTree(postfix)
    ans = expTree.evaluate()
    testObj.assertEqual(ans, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   ["3","4","+","2","*","7","/"], 2)

    def test_2(self):
        test(self,   ["4","5","2","7","+","-","*"], -16)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 40 ms, faster than 87.00% of Python3 online submissions for Design an Expression Tree With Evaluate Function.
Memory Usage: 14 MB, less than 16.63% of Python3 online submissions for Design an Expression Tree With Evaluate Function.
'''
