class BSTNode:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left_count = 0
        self.left = None
        self.right = None

    def insert(self, val):
        # return the number of elements in the current BST that is less than val
        if val == self.val:
            self.count += 1
            return self.left_count
        elif val < self.val:
            self.left_count += 1
            if self.left is None:
                self.left = BSTNode(val)
                return 0
            else:
                return self.left.insert(val)
        else:
            # val > self.val
            if self.right is None:
                self.right = BSTNode(val)
                return self.count + self.left_count
            else:
                return self.count + self.left_count + self.right.insert(val)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        rev_nums = reversed(nums[:-1])
        ans = [0]
        root = BSTNode(nums[-1])
        for num in rev_nums:
            ans.append(root.insert(num))
        ans.reverse()
        return ans
