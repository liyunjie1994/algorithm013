class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        left = 0
        right = 0
        S = ''
        str(S)
        def generate(left, right, S):
######终止条件
            if left == n and right == n:
                ans.append(S)
#######当前状态,递归向下更深一层
            if left < n:
                S = S + '('
                generate(left + 1, right, S)

            if right < left:
                S = S + ')'
                generate(left, right + 1, S)
#####generate递归函数回归初始
        generate(0, 0, '')
        return ans
