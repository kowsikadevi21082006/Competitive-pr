class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powerlen = pow(power, k-1, modulo)
        current = sum([ (ord(s[len(s)- k + i]) - 96) * pow(power, i, modulo) for i in range(k) ])
        index = len(s) - k
        for i in range(len(s)-k-1, -1, -1):
            current = current-(ord(s[i+k]) - 96) * powerlen
            current = current * power
            current += (ord(s[i]) - 96)
            current = current % modulo
            if current == hashValue: index = i
        return s[index:index+k]