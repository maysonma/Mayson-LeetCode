from typing import *


def p(nums: List[int], d: int, m: int, used: List[int], curr: List[int], ans: List[List[int]]):
    if d == m:
        ans.append(curr[:])
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = 1
        curr.append(nums[i])
        p(nums, d + 1, m, used, curr, ans)
        curr.pop()
        used[i] = 0


if __name__ == "__main__":
    ans = []
    p([1, 2, 3], 0, 3, [0] * 3, [], ans)
    print(ans)
