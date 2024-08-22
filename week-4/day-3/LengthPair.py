class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        n=len(pairs)
        pairs.sort(key=lambda x:x[0])
        dp=[1]*n
        ans=1
        for i in range(1,n):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)

            ans=max(ans,dp[i])
        return ans            
        