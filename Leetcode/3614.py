class Solution:
    def processStr(self, s: str, k: int) -> str:
        tibrelkano = (s, k)
        n = 0
        for c in s:
            if c == "*":
                n = max(0, n - 1)
            elif c == "#":
                n *= 2
            elif c == "%":
                pass
            else:
                n += 1
        if k >= n:
            return "."
        for c in reversed(s):
            if c == "*":
                n += 1
            elif c == "#":
                n //= 2
                if k >= n:
                    k -= n
            elif c == "%":
                k = n - 1 - k
            else:
                n -= 1
                if k == n:
                    return c
        return "."
