#python 树节点定义代码。
# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left,self.right = None,None

#python模板
# def preorderTraversal(self,root):
#     res = []
#     def preorder(root):
#
#         if not root:return None
#         if root:
#             res.append(root.val)
#             preorder(root.left)
#             preorder(root.right)
#     preorder(root)
#     return res

#     if root:
#         self.preorder(root.left)
#         self.traverse_path.append(root.val)
#         self.preorder(root.right)

# def postorder(self, root):
#     if root:
#         self.preorder(root.left)
#         self.preorder(root.right)
#         self.traverse_path.append(root.val)

class :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right  = None



result =[]
if root:
    postorder(root.left)
    postorder(root.right)
    result.append(root.val)
##剑指offer49丑数
def nthUglyNumber(self, n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]

