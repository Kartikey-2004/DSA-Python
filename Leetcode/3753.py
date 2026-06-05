from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, tight, started, prev1, prev2):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_sum = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, 10, 10)
                        total_cnt += cnt
                        total_sum += wav
                    else:
                        extra = 0

                        if started and prev2 != 10:
                            y = prev1
                            x = prev2

                            if (y > x and y > d) or (y < x and y < d):
                                extra = 1

                        cnt, wav = dfs(
                            pos + 1, ntight, True, d, prev1 if started else 10
                        )

                        total_cnt += cnt
                        total_sum += wav + extra * cnt

                return total_cnt, total_sum

            return dfs(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)
