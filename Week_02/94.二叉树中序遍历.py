def preorderTraversal(self,root):
    res = []
    def preorder(root):

        if not root:return None
        if root:
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
    preorder(root)
    return res