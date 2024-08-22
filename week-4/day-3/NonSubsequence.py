class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        ans = {}
        
        def rec(idx, arr):
            if len(arr) > 1: ans[tuple(arr)]= 1
                
            for i in range(idx, N):
                if nums[i] >= arr[-1]:
                    rec(i+1, arr+[nums[i]])
        
        for i in range(N): 
            rec(i+1, [nums[i]])
            
        return ans.keys()