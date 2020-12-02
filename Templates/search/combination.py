def c(nums, d, m, s, curr, ans):
    if d == m:
        ans.append(curr[:])
        return
    for i in range(s, len(nums)):
        curr.append(nums[i])
        c(nums, d + 1, m, i + 1, curr, ans)
        curr.pop()


if __name__ == "__main__":
    ans0 = []
    c([1, 2, 3], 0, 2, 0, [], ans0)
    print(ans0)
