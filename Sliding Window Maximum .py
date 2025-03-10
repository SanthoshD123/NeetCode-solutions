class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums or k == 0: 
            return res
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
