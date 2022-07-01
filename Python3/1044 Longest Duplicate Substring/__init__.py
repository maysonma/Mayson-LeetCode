from collections import defaultdict

PRIME = int(1e9 + 7)
BASE = 256


def rabin_karp(s, m):
    if m <= 0:
        return ""
    largest_base = pow(BASE, m - 1, PRIME)
    hs = 0
    for char in s[:m]:
        hs = (hs * BASE + ord(char)) % PRIME

    dic = defaultdict(list)
    dic[hs].append(m - 1)

    for i in range(m, len(s)):
        deleted_char = s[i - m]
        hs = ((hs - largest_base * ord(deleted_char)) * BASE + ord(s[i])) % PRIME
        for end in dic[hs]:
            if s[end - m + 1:end + 1] == s[i - m + 1:i + 1]:
                return s[i - m + 1:i + 1]
        dic[hs].append(i)

    return ""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        start, end = 1, len(s) - 1
        ans = ""
        while start <= end:
            mid = start + (end - start) // 2
            substr = rabin_karp(s, mid)
            if substr:
                ans = substr
                start = mid + 1
            else:
                end = mid - 1
        return ans
