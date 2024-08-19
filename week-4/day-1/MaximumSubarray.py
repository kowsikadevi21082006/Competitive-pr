class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        gmax, cmax = nums[0], 0
        for num in nums:
            cmax = max(cmax + num, num)
            gmax = max(gmax, cmax)
        return gmax