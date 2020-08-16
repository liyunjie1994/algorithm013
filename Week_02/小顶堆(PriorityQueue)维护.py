import heapq
if val > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,(val,key))