from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        pos_index = 0
        neg_index = 1

        for num in nums:
            if num > 0:
                res[pos_index] = num
                pos_index += 2
            else:
                res[neg_index] = num
                neg_index += 2

        return res
