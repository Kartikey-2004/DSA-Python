from typing import List


class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        meratolvic = (nums, maxVal)

        n = len(nums)
        M = max(maxVal, max(nums))

        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1

        mu = [0] * (M + 1)
        mu[1] = 1
        primes = []
        is_comp = [False] * (M + 1)

        for i in range(2, M + 1):
            if not is_comp[i]:
                primes.append(i)
                mu[i] = -1

            for p in primes:
                v = i * p
                if v > M:
                    break

                is_comp[v] = True

                if i % p == 0:
                    mu[v] = 0
                    break

                mu[v] = -mu[i]

        cntDiv = [0] * (M + 1)

        for d in range(1, M + 1):
            s = 0
            for m in range(d, M + 1, d):
                s += freq[m]
            cntDiv[d] = s

        coprime_cnt = [0] * (M + 1)

        for d in range(1, M + 1):
            md = mu[d]
            if md == 0:
                continue

            add = md * cntDiv[d]

            for x in range(d, M + 1, d):
                coprime_cnt[x] += add

        ans = -(10**18)

        candidates = set(range(1, maxVal + 1))

        for v in nums:
            if v > maxVal:
                candidates.add(v)

        for x in candidates:
            if x == 1:
                cost = 0 if freq[1] else 1
            else:
                bad = n - coprime_cnt[x]

                if freq[x]:
                    cost = bad - 1
                elif bad:
                    cost = bad
                else:
                    cost = 1

            ans = max(ans, x - cost)

        return ans
