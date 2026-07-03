class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        ans = 0

        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
            ans += min(last) + 1

        return ans
