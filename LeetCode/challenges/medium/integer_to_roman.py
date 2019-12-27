from collections import OrderedDict
from math import log, ceil


class Solution:
    def __init__(self):
        self.numeral_table = OrderedDict()

        self.numeral_table[1000] = 'M'
        self.numeral_table[500] = 'D'
        self.numeral_table[100] = 'C'
        self.numeral_table[50] = 'L'
        self.numeral_table[10] = 'X'
        self.numeral_table[5] = 'V'
        self.numeral_table[1] = 'I'

    def intToRoman(self, num: int) -> str:
        roman_numeral = ''
        numeral_table = list(self.numeral_table.items())
        i = 0

        while i < len(numeral_table):
            numeral = numeral_table[i][1]
            value = int(numeral_table[i][0])
            num_numeral = num // value

            if num_numeral > 0:
                roman_numeral += (numeral * num_numeral)
                num = num % value
            else:
                possible_subtractor = 10 ** (ceil(log(value, 10)) - 1)

                if num // (value - possible_subtractor) == 1:
                    roman_numeral += self.numeral_table[possible_subtractor] + numeral
                    num = num % (value - possible_subtractor)
                i += 1

        return roman_numeral


if __name__ == '__main__':
    print(Solution().intToRoman(1994))
