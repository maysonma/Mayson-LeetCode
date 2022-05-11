class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def apply_backspace(string, end):
            if end < 0 or string[end] != '#':
                return end
            count = 1
            r = end - 1
            while r >= 0 and count > 0:
                if string[r] == '#':
                    count += 1
                else:
                    count -= 1
                r -= 1
            return apply_backspace(string, r)

        ptr1 = len(s) - 1
        ptr2 = len(t) - 1
        while True:
            ptr1 = apply_backspace(s, ptr1)
            ptr2 = apply_backspace(t, ptr2)
            if ptr1 < 0 and ptr2 < 0:
                return True
            elif ptr1 >= 0 and ptr2 >= 0:
                if s[ptr1] == t[ptr2]:
                    ptr1 -= 1
                    ptr2 -= 1
                    continue
                else:
                    return False
            else:
                return False

if __name__ == "__main__":
    s = Solution()
    ans = s.backspaceCompare("ab#c", "ad#c")
    print(ans)
