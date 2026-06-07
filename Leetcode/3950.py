class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        while n > 0:
            if (n & 3) == 3:
                count += 1
            n >>= 1

        return count == 1
