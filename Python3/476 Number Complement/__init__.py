class Solution:
    def findComplement(self, num: int) -> int:
        bit_count = 1
        n = num >> 1
        while n > 0:
            bit_count += 1
            n = n >> 1

        all_bits_set = pow(2, bit_count) - 1
        return all_bits_set ^ num
