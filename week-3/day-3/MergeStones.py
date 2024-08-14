class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        
        n = len(stones)

        if (n-1)%(k-1): return -1
        pref = [0 for i in range(n+1)]

        for i in range(1,n+1):
            pref[i] = pref[i-1] + stones[i-1]
        

        def pref_sum(l,r):
            return pref[r+1]-pref[l]

        inf = int(2e9)

        # @cache
        def solve(i,j):
    
            if j-i+1 < k:
                return 0,j-i+1
            val,sz = inf,1
            for l in range(i,j):
                left,lsz = solve(i,l)
                right,rsz = solve(l+1,j)
                if lsz+rsz<k:
                    if left+right<val:
                        val,sz = left+right,lsz+rsz
                        
                
                if lsz+rsz == k:
                    if left+right+pref_sum(i,j)<val:
                        val,sz = left+right+pref_sum(i,j),1

            return val,sz

        return solve(0,n-1)[0]
       

            
            