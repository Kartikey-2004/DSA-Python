from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for num in cnt:
            if num == 1:
                continue

            x = num
            length = 0

            while cnt.get(x, 0) >= 2:
                length += 2
                x *= x

            if cnt.get(x, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
