from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSumCount = {}
        prefixSum = 0
        count = 0

        prefixSumCount[0] = 1

        for i in range(n):
            prefixSum += nums[i]
            remove = prefixSum - k

            if remove in prefixSumCount:
                count += prefixSumCount[remove]

            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1

        return count
