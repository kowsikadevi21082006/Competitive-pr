class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2  
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k