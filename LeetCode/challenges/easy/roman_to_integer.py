class Solution:
    def __init__(self):
        self.numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.combo_numerals = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

    def romanToInt(self, s: str) -> int:
        num = 0
        while s:
            if len(s) > 1 and s[0:2] in self.combo_numerals:
                num += self.combo_numerals[s[0:2]]
                s = s[2:]
            else:
                num += self.numerals[s[0]]
                s = s[1:]
        return num