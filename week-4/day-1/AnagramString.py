class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        d = {}
        for c in p:
            d.setdefault(c, 0)
            d[c] += 1
        
        output = []
        head = 0
        tail = 0
        while tail < len(s):
            if s[tail] not in d:
                while head < tail:
                    d[s[head]] += 1
                    head += 1
                head = tail = tail + 1
            elif d[s[tail]] == 0:
                d[s[head]] += 1
                head += 1
            else:
                d[s[tail]] -= 1
                tail += 1
            
            if tail - head == len(p):
                output.append(head)
                d[s[head]] += 1
                head += 1
        return output
        