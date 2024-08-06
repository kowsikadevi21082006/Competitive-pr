class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        ans=0
        for i,num in enumerate(nums):
            d=num%10
            for j in range(i):
                n=nums[j]
                while n>=10:
                    n//=10

                ans+=(d,n)==1

        return ans        