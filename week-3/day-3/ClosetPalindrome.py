class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def generatePalindrome(s):        
            results = [i for i in s]
            for i in range(len(s)//2):
                results[len(s) - i - 1] = s[i]
            return int(''.join(results))

        def loop20(mid):
            p = []
            for i in range(-10, 11):
                if int(n[:mid]) + i >= 0:
                    p.append(generatePalindrome(str(int(n[:mid]) + i) + n[mid:]))        
            return p
        
        mid = len(n)//2 + 1
        p = loop20(mid)
        p.sort(reverse=True)
        
        minPalindromeIndex, minDiff = '', float('inf')
        for i in range(len(p)):
            if p[i] != int(n) and abs(p[i] - int(n)) <= minDiff:
                minPalindromeIndex, minDiff = i, abs(p[i] - int(n))
        
        return str(p[minPalindromeIndex])