import math


class Solution:
    def exactly3Divisors(self, n: int) -> int:

        limit = int(math.isqrt(n))

        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        count = sum(1 for i in range(2, limit + 1) if is_prime[i])
        return count
