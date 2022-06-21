from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = set(wordList)
        q = [beginWord]
        if endWord not in word_dict:
            return 0
        step = 0
        n = len(beginWord)
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        while q:
            step += 1
            nxt_q = []
            for node in q:
                for i in range(n):
                    for char in alphabet:
                        tmp = node[:i] + char + node[i + 1:]
                        if tmp not in word_dict:
                            continue
                        if tmp == endWord:
                            return step + 1
                        nxt_q.append(tmp)
                        word_dict.remove(tmp)
            q = nxt_q
        return 0
