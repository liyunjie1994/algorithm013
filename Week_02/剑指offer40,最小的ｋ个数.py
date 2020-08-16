import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        res = []
        max_arr = [-x for x in arr[:k]]
        ##python heapify生成的小顶堆
        heapq.heapify(max_arr)
        for j in range(k, len(arr)):
            if -arr[j] > max_arr[0]:
                heapq.heappop(max_arr)
                heapq.heappush(max_arr, -arr[j])
        for n in range(k):
            res.append(max_arr[n])
        return res
