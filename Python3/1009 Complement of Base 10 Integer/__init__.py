class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit_count = 1
        m = n >> 1
        while m > 0:
            bit_count += 1
            m = m >> 1

        all_bits_set = pow(2, bit_count) - 1
        return all_bits_set ^ n
