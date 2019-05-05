from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        s = 0  # start position

        def get_name():
            nonlocal formula, s, n
            i = s + 1
            while i < n and formula[i].islower():
                i += 1
            name = formula[s:i]
            s = i
            return name

        def get_num():
            nonlocal formula, s, n
            if s == n or not formula[s].isdigit():
                return 1
            i = s + 1
            while i < n and formula[i].isdigit():
                i += 1
            num = int(formula[s:i])
            s = i
            return num

        def count_atom():
            nonlocal formula, s, n
            atom_dict = defaultdict(int)
            while s < n:
                if formula[s] == '(':
                    s += 1
                    r_dict = count_atom()
                    num = get_num()
                    for a in r_dict:
                        atom_dict[a] += r_dict[a] * num
                elif formula[s] == ')':
                    s += 1
                    return atom_dict
                else:
                    name = get_name()
                    num = get_num()
                    atom_dict[name] += num
            return atom_dict

        r_dict = count_atom()
        ans = ''
        for atom in sorted(r_dict.keys()):
            ans += atom
            num = r_dict[atom]
            if num > 1:
                ans += str(num)
        return ans
