class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # helper func
        def partition(nums, l, r):
            pivot = nums[r]
            idx = l
            for i in range(l, r):
                if nums[i] > pivot:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1
            nums[idx], nums[r] = nums[r], nums[idx]
            return idx

        # main
        if len(nums) < k: return -1
        l = 0
        r = len(nums) - 1
        random.shuffle(nums)
        while True:
            pos = partition(nums, l, r)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                r = pos - 1
            else:
                l = pos + 1
