import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) - k > 0:
            heapq.heappop(nums)

        return heapq.heappop(nums)
