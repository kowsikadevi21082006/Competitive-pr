class Solution:
    def minimizeResult(self, expre: str) -> str:
        plus_index, n, ans = expre.find('+'), len(expre), [float('inf'),expre] 
        def evaluate(exps: str):
            return eval(exps.replace('(','*(').replace(')', ')*').lstrip('*').rstrip('*'))
        for l in range(plus_index):
            for r in range(plus_index+1, n):
                exps = f'{expre[:l]}({expre[l:plus_index]}+
                {expre[plus_index+1:r+1]}){expre[r+1:n]}'
                res = evaluate(exps)
                if ans[0] > res:
                    ans[0], ans[1] = res, exps
        return ans[1]