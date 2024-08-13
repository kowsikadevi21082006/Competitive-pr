class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        result = [i for i in range(len(s)) if s.startswith(a, i)]
        if a.startswith(b):
            return result
        m = len(b)
        if not result:
            return []
        j = None
        j_start = 0
        beautiful = []
        for i in result:
            j_start = max(j_start, i - k)
            if j is None or j_start< i+k:
                j = next((n for n in range(j_start, i+k+1) if s[n:n+m] == b), None)
            if j is None:
                continue
            j_start = j
            beautiful.append(i)
        return beautiful