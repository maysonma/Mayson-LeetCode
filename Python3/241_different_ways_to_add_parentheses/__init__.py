import operator
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul, }
        mem = {}

        def compute_rec(expr):
            nonlocal ops, mem
            if expr in mem:
                return mem[expr]
            result = []
            if expr.isdigit():
                result.append(int(expr))
            else:
                for i in range(len(expr)):
                    if expr[i] in ops:
                        left = compute_rec(expr[:i])
                        right = compute_rec(expr[i + 1:])
                        result.extend([ops[expr[i]](l, r) for l in left for r in right])
            mem[expr] = result
            return result

        return compute_rec(expression)
