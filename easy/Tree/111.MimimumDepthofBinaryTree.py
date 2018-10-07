'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

'''
Summary:
difficultly is the node with only one child note is not leaf. 
Compare with 104. Maximum Depth of Binary Tree 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0 
        
        left = self.minDepth(root.left) + 1 
        right = self.minDepth(root.right) + 1
        
        if root.left == None or root.right == None : 
            return max(left, right)
        else : 
             return min(left, right)
            
        