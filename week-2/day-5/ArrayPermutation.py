class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(nums[nums[i]])
        return answer
        