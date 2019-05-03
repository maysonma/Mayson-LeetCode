class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(nums, s, cur, ans):
            if len(cur) == 4:
                if s == len(nums):
                    ans.append('.'.join(cur))
                return
            if (4 - len(cur)) * 3 < len(nums) - s:
                return
            if s == len(nums):
                return
            if nums[s] == '0':
                cur.append(nums[s])
                dfs(nums, s + 1, cur, ans)
                cur.pop()
                return
            for i in range(s + 1, min(s + 3 + 1, len(nums) + 1)):
                tmp = nums[s:i]
                if int(tmp) <= 255:
                    cur.append(tmp)
                    dfs(nums, i, cur, ans)
                    cur.pop()

        ans = []
        dfs(s, 0, [], ans)
        return ans
