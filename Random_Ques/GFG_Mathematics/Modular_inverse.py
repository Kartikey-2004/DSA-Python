class Solution:
    def modInverse(self, n: int, m: int) -> int:
        
        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0
            gcd, x1, y1 = extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

        gcd, x, y = extended_gcd(n, m)
        if gcd != 1:
            return -1
        return x % m
