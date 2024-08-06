class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        max_bit=17
        child=dict(list)
        for i,p in enumerate(parents):
            child[p].append(i)
        cnt=dict(int)
        q_by_c=dict(list)
        for i,(c,_) in enumerate(queries):
            q_by_c[c].append(i)
        res=[-1]*len(queries)
        def traverse(p):
            if p>=0:
                for l in range(max_bit+1):
                    cnt[l,p>>l]+=1
            for i in q_by_c[p]:
                val=queries[i][1]
                mask=0
                for l in range(max_bit,-1,-1):
                    val_l = val>>l
                    mask0=mask<<1
                    mask1=mask0+1
                    mask=mask1 if cnt[l,val_l^mask1]>0 else mask0
                res[i]=mask
            for c in child[p]:
                traverse(c)
            if p>=0:
                for l in range(max_bit+1):
                    cnt[l,p>>l]-=1            
        traverse(-1)
        return res