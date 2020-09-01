# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        ###终止条件,inorder中子树被分完了
        if inorder:

            root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_index])

            ##递归中,preoder每pop出的元素是子树的子根
            root.left = self.buildTree(preorder,inorder[:root_index])
            root.right = self.buildTree(preorder,inorder[root_index+1:])

            return root