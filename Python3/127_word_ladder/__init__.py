from collections import deque
from typing import List


class Solution:
    def ladderLength_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = {w: False for w in wordList}
        if endWord not in seen:
            return 0
        seen[beginWord] = True

        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        queue = deque()
        seq_len = 0
        queue.append(beginWord)
        n = len(beginWord)

        while queue:
            cur_level = len(queue)
            seq_len += 1
            for _ in range(cur_level):
                u = queue.popleft()
                if u == endWord:
                    return seq_len
                for i in range(n):
                    for c in alphabet:
                        succr = u[:i] + c + u[i + 1:]
                        if not seen.get(succr, True):
                            queue.append(succr)
                            seen[succr] = True

        return 0

    def ladderLength_bdbfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = {w: False for w in wordList}
        if endWord not in seen:
            return 0
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        n = len(beginWord)
        seen[beginWord] = seen[endWord] = True
        s1, s2 = {beginWord}, {endWord}
        seq_len = 0
        while s1 and s2:
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            seq_len += 1
            s = set([])
            for u in s1:
                for i in range(n):
                    for c in alphabet:
                        succr = u[:i] + c + u[i + 1:]
                        if succr in s2:
                            return seq_len + 1
                        if not seen.get(succr, True):
                            s.add(succr)
                            seen[succr] = True
            s1 = s
        return 0
