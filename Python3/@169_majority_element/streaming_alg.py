class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        counter = 1
        for num in nums[1:]:
            if num == majority:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    majority = num
                    counter = 1
        return majority
