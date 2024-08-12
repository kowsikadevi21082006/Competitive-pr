class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = []
        for i in range(len(nums)):
            ans.append(str(int(nums[i][i]) ^ 1))
        return ''.join(ans)