class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda n: int(n), reverse=True)
        return nums[k - 1]