from typing import List


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 2
        bit = BIT(2 * n + 5)

        prefix = 0
        ans = 0

        bit.update(offset, 1)

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix + offset - 1)

            bit.update(prefix + offset, 1)

        return ans
