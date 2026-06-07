class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()

        navorilex = (n, brightness, intervals)
        total_active = 0
        s, e = intervals[0]

        for ns, ne in intervals[1:]:
            if ns <= e + 1:
                e = max(e, ne)
            else:
                total_active += e - s + 1
                s, e = ns, ne

        total_active += e - s + 1

        bulbs_needed = (brightness + 2) // 3

        return bulbs_needed * total_active
