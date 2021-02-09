import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input
        nums = nums.copy()
        if not nums:
            root = None
        else:
            root = TreeNode(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num is not None:
                    curr_node.left = TreeNode(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num is not None:
                    curr_node.right = TreeNode(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        root = self.bstToGst(root)
        ans = []
        l = [root]
        while l:
            node = l.pop(0)
            if node:
                ans.append(node.val)
            else:
                ans.append(None)
            if node and node.left:
                l.append(node.left)
            elif node:
                l.append(None)
            if node and node.right:
                l.append(node.right)
            elif node:
                l.append(None)
            if all(v is None for v in l):
                break
        return ans

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node, s):
            if not node:
                return s
            s = inorder(node.right, s)
            s += node.val
            node.val = s
            return inorder(node.left, s)

        inorder(root, 0)
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
