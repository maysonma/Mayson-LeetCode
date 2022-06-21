from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        word_set.remove(endWord)
        s1 = {beginWord}
        s2 = {endWord}
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        n = len(beginWord)
        step = 0
        while len(s1) and len(s2):
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set([])
            for node in s1:
                for i in range(n):
                    for char in alphabet:
                        tmp = node[:i] + char + node[i + 1:]
                        if tmp in s2:
                            return step + 1
                        if tmp not in word_set:
                            continue
                        s.add(tmp)
                        word_set.remove(tmp)
            s1 = s
        return 0
