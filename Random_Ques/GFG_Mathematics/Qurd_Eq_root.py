import math
from typing import List


class Solution:
    def quadraticRoots(self, a: int, b: int, c: int) -> List[int]:
        # code here
        D = b * b - 4 * a * c
        if D < 0:
            return [-1]

        sqrt_D = math.sqrt(D)

        root_1 = math.floor((-b + sqrt_D) / (2 * a))
        root_2 = math.floor((-b - sqrt_D) / (2 * a))

        return [root_1, root_2]
