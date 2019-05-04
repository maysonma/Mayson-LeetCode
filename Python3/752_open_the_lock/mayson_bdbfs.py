class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if target in dead or "0000" in dead:
            return -1
        s1 = set(['0000'])
        s2 = set([target])
        neighbor = {'0': ['1', '9'], '9': ['8', '0']}
        for i in range(1, 9):
            neighbor[str(i)] = [str(i - 1), str(i + 1)]
        step = -1
        n = 4
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set([])
            for node in s1:
                num = int(node)
                for i in range(n):
                    for char in neighbor[node[i]]:
                        tmp = node[:i] + char + node[i + 1:]
                        if tmp in dead:
                            continue
                        if tmp in s2:
                            return step + 1
                        s.add(tmp)
            s1 = s
        return -1
