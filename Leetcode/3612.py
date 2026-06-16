class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch == "*":
                if res:
                    res.pop()
            elif ch == "#":
                res.extend(res)
            else:  # '%'
                res.reverse()
        return "".join(res)
