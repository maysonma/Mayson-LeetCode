class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(50):
            counter = 0
            thed = len(nums) // 2
            candidate = nums[random.randint(0, len(nums) - 1)]
            for num in nums:
                if num == candidate:
                    counter += 1
                    if counter > thed:
                        return candidate
        return -1
