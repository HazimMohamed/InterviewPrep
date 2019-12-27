class Solution:
    def myAtoi(self, s: str) -> int:
        if s.strip() == '':
            return 0

        table = "0123456789"

        x, k = 0, 0
        while s[k] not in table and s[k] != '+' and s[k] != '-':
            if s[k] != ' ':
                return 0
            k += 1

        multiplier = 1
        if s[k] == '+':
            k += 1
        elif s[k] == '-':
            multiplier = -1
            k += 1

        while k < len(s) and s[k] in table:
            x *= 10
            x += table.find(s[k])
            k += 1

        if x < 2 ** 31:
            return x * multiplier
        else:
            return 2 ** 31 * multiplier - 1 if multiplier == 1 else 0

print(Solution().myAtoi('-91283472332'))