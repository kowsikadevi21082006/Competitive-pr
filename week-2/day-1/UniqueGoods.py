class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        ans = [0]*2

        for i in binary:
            ans[int(i)] = sum(ans) + int(i)

        return (sum(ans) + ("0" in binary))%(10**9+7)




