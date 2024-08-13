class Solution:
    def maxLength(self, arr: list[str]) -> int:
        exclusive = set([i for i, a in enumerate(arr) if len(set(a)) != len(a)])
        res = 0
        def f(i, S):
            nonlocal res
            if i < len(arr):
                T = set(arr[i])
                if not (T & S) and i not in exclusive:
                    U = T | S
                    res = max(res, len(U))
                    f(i+1, U)
                f(i+1, S)
        f(0, set())
        return res
        