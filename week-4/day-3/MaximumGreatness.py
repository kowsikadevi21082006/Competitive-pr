class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()
        ans=0
        for num in nums:
            if num>nums[ans]:
                ans+=1

        return ans        
        