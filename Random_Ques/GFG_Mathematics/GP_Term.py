class Solution:
    def termOfGP(self, a: int, b: int, n: int) -> int:

        r = b / a
        term = a * (r ** (n - 1))
        return term
