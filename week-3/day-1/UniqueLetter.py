class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = [0] * (len(s) + 1)
        index = [[-1, -1]] * 26
        for i, c in enumerate(s):
            code = ord(c) - ord('A')
            first, second = index[code]
            result[i + 1] = 1 + result[i] + (i - 1 - second) - (second - first)
            index[code] = [second, i]
        return sum(result) % (10 ** 9 + 7)
        