# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def inOrder(self, root,ans):

        if not root:
            return None
        if root:
            self.inOrder(root.left,ans)
            ans.append(root.val)
            self.inOrder(root.right,ans)
        return ans


    def isValidBST(self, root):
        ans = []
        self.inOrder(root,ans)
        for i in range(len(ans)-1):
            if ans[i] > ans[i+1]:
                return  False
        return True

