class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        m = r - l + 1
        size = 2 * m

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                Ai = A[i]
                Ci = C[i]
                for k in range(size):
                    if Ai[k] == 0:
                        continue
                    a = Ai[k]
                    Bk = B[k]
                    for j in range(size):
                        if Bk[j]:
                            Ci[j] = (Ci[j] + a * Bk[j]) % MOD
            return C

        def mat_pow(M, p):

            R = [[0] * size for _ in range(size)]
            for i in range(size):
                R[i][i] = 1
            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1
            return R

        def mat_vec_mul(M, v):
            res = [0] * size
            for i in range(size):
                s = 0
                row = M[i]
                for j in range(size):
                    if row[j]:
                        s = (s + row[j] * v[j]) % MOD
                res[i] = s
            return res

        T = [[0] * size for _ in range(size)]
        for x in range(m):
            for y in range(x):
                T[x][m + y] = 1
            for y in range(x + 1, m):
                T[m + x][y] = 1
        init = [1] * size
        P = mat_pow(T, n - 1)
        final_state = mat_vec_mul(P, init)
        return sum(final_state) % MOD
