class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if not nums or sum(nums) < target:
            return 0
        dic = {0:1}
        for i in range(len(nums)):
            temp = {}
            for k in dic:
                if k + nums[i] in temp:
                    temp[k + nums[i]] += dic[k]
                else:
                    temp[k + nums[i]] = dic[k]
                if k - nums[i] in temp:
                    temp[k-nums[i]] += dic[k]
                else:
                    temp[k-nums[i]] = dic[k]
            dic = temp
        if target in dic:
            return dic[target]
        else:
            return 0
        