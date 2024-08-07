class Solution:
    def countPrefixSuffixPairs(self, w: list[str]) -> int:
        count = 0
        for i in range(len(w)):
            t = len(w[i])
            for j in range(i+1,len(w)):
                if len(w[j])>=t:
                    if w[j][:t]==w[i] and w[j][-t:]==w[i]:
                        count+=1
        return count