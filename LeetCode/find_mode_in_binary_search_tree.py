# https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=daily-question&envId=2023-11-01

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


# def inorder(node):
#     if node is not None:
#         inorder(node.left)
#         print(node.data)
#         inorder(node.right)
# # Inorder traversal of the tree
# inorder(root)

class Solution:
 
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.findMode(root.left)
            self.findMode(root.right)

