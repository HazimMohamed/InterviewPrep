class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # diff row 1 is 4 - 0
        # diff row 2 is 2 - 2
        # diff row 3 is 0 - 4

        # diff row 1 is 6 - 0
        # diff row 2 is 4 - 2
        # diff row 3 is 2 - 4
        # diff row 4 is 0 - 6

        # diff row 1 is 8 - 0
        # diff row 2 is 6 - 2
        # diff row 3 is 4 - 4
        # diff row 4 is 2 - 6
        # diff row 5 is 0 - 8

        # P    H
        # A   S I
        # Y  I   R
        # P L     I G
        # A        N

        # 0, 6, 12,
        # 1, 5, 7, 11, 13,
        # 2, 4, 8, 10
        # 3, 9

        if numRows == 1:
            return s

        encoded = ''
        increment = ((numRows - 1) * 2, 0)
        for i in range(numRows):
            x = i
            iteration = 0
            while x < len(s):
                inc = increment[iteration % 2]
                if inc != 0:
                    encoded += s[x]
                    x += inc
                iteration += 1
            increment[0] -= 2
            increment[1] += 2
        return encoded
