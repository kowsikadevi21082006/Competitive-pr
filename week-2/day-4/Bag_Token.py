class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        r=score=0
        tokens.sort()
        i,j= 0,len(tokens)-1
        while i<=j:
            if power>=tokens[i]:
                score+=1
                power-=tokens[i]
                i+=1
                r=max(r,score)
            elif score>0:
                score-=1
                power+=tokens[j]
                j-=1
            else: 
                break
        return r