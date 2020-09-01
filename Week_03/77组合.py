def combine(self,n,k):
    if n <= 0 or k <= 0 or k > n:
        return []
    res = []
    self.__dfs(1,k,n,[],res)
    return res

def _dfs(self,start,k,n,pre,res):
    if len(pre) == k:
        res.append(pre[:])
        return

    for i in range(start,n+1):
        pre.append(i)
        self.__dfs(i + 1, k, n, pre, res)
        pre.pop()