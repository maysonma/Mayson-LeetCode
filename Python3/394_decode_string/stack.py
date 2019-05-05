class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ''
        stack = []
        for ch in s:
            if ch == '[':
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif ch == ']':
                pre_str, pre_num = stack.pop()
                cur_str = pre_str + pre_num * cur_str
            elif ch.isdigit():
                cur_num = 10 * cur_num + int(ch)
            else:
                cur_str += ch
        return cur_str
