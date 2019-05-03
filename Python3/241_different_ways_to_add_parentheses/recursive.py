from itertools import product


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        m_ = {}
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y}

        def ways(expr):
            nonlocal m_, ops
            if expr in m_:
                return m_[expr]
            res = []
            for idx, char in enumerate(expr):
                if char in ops:
                    l = ways(expr[:idx])
                    r = ways(expr[idx + 1:])
                    res.extend([ops[char](v1, v2) for v1, v2 in product(l, r)])
            if not res:
                res.append(int(expr))
            m_[expr] = res
            return res

        return sorted(ways(input))
