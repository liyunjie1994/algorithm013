class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            t=tuple(sorted(i))
            d[t]= d.get(t,[])
            d[t].append(i)
        return list(d.values())