from bisect import bisect_right
from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def solve(start1, dur1, start2, dur2):
            rides = sorted(zip(start2, dur2))
            starts = [s for s, _ in rides]

            m = len(rides)

            pref = [0] * m
            pref[0] = rides[0][1]

            for i in range(1, m):
                pref[i] = min(pref[i - 1], rides[i][1])

            suff = [0] * m
            suff[-1] = rides[-1][0] + rides[-1][1]

            for i in range(m - 2, -1, -1):
                suff[i] = min(suff[i + 1], rides[i][0] + rides[i][1])

            ans = float("inf")

            for s, d in zip(start1, dur1):
                finish = s + d

                idx = bisect_right(starts, finish) - 1

                if idx >= 0:
                    ans = min(ans, finish + pref[idx])

                if idx + 1 < m:
                    ans = min(ans, suff[idx + 1])

            return ans

        return min(
            solve(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration,
            ),
            solve(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration,
            ),
        )
