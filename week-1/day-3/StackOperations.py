class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        N=[i for i in range(1,n+1)]
        for i in range(len(N)):
            if N[i] in target:
                stack.append('Push')
            if N[i] not in target:
                c=0
                for k in range(i+1,len(N)):
                    if N[k] in target:
                        c=1
                        break
                if c==1:
                    stack.append('Push')
                    stack.append('Pop')
                else:
                    return stack
        return stack