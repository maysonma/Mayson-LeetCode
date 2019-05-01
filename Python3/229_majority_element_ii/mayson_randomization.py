class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        ans = []
        thrd = len(nums) // 3
        for i in range(10):
            if len(ans) == 2:
                return ans
            candidate = nums[random.randint(0, len(nums) - 1)]
            if candidate in ans:
                continue
            counter = 0
            for num in nums:
                if num == candidate:
                    counter += 1
                    if counter > thrd:
                        ans.append(candidate)
                        break
        return ans
