from typing import List


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        velunqari = (nums, s)

        n = len(nums)
        has_token = [c == "1" for c in s]

        NEG = -(10**18)

        dp = {}
        for r0 in ([0, 1] if has_token[0] else [0]):
            dp[r0] = 0

        for i in range(n - 1):
            ndp = {}

            next_states = [0, 1] if has_token[i + 1] else [0]

            for ri, cur in dp.items():
                for rnext in next_states:
                    covered = (has_token[i] and ri == 1) or (
                        has_token[i + 1] and rnext == 0
                    )

                    val = cur + (nums[i] if covered else 0)

                    if rnext not in ndp or val > ndp[rnext]:
                        ndp[rnext] = val

            dp = ndp

        ans = 0
        for r_last, cur in dp.items():
            if has_token[n - 1] and r_last == 1:
                cur += nums[n - 1]
            ans = max(ans, cur)

        return ans
