import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        for freq, num in heap:
            res.append(num)
            
        return res