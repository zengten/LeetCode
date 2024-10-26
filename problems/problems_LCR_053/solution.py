import solution
from typing import *
from python.object_libs import list_to_tree, list_to_tree_with_target, tree_to_list


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, num1 = test_input
        nodes = list_to_tree_with_target(nums0, num1)
        root0 = nodes[0]
        node1 = nodes[1]
        res = self.inorderSuccessor(root0, node1)
        return tree_to_list(res)

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        pass

