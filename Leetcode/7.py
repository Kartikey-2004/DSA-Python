class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1
        int_min = -(2**31)

        rev = 0

        while x != 0:
            digit = int(x % 10) if x > 0 else (x % -10)
            x = int(x / 10)

            if rev > int_max // 10 or (rev == int_max // 10 and digit > 7):
                return 0
            
            if rev < int_min // 10 or (rev == int_min // 10 and digit < 8):
                return 0

            rev = rev * 10 + digit

        return rev
