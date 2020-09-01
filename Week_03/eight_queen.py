##3.current state
##4.drill down

def solveNQueens(self,n):
    result = []

    def DFS(queens,xy_dif,xy_sum):
        ###下面这句不懂
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        ####遍历一行中的所有列.这里列用q来表示
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                DFS(queens+[q], xy_dif + [p-q], xy_sum + [p+q])

    DFS([],[],[])
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
