from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = [list(word)]
        for i in range(len(word)):
            n = len(result)
            for j in range(n):
                old = result[j]
                if i == 0 or (i > 0 and old[i - 1].isalpha()):
                    new = list(old)
                    new[i] = '1'
                    result.append(new)
                else:
                    k = i - 1
                    while not old[k].isdigit():
                        k -= 1
                    new = list(old)
                    new[k] = str(int(old[k]) + 1)
                    new[i] = ''
                    result.append(new)
        result = [''.join(w) for w in result]
        return result
