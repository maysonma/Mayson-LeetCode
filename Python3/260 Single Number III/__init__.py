from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num

        right_most_bit = 1
        while right_most_bit & n1xn2 == 0:
            right_most_bit <<= 1

        num1 = num2 = 0
        for num in nums:
            if num & right_most_bit == 0:  # not set:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
