import math


class Solution:
    def digitsInFactorial(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1

        x = n * math.log10(n / math.e) + 0.5 * math.log10(2 * math.pi * n)
        return math.floor(x) + 1
