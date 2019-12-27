class Solution:
    def __init__(self):
        self.partner_table = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

    def isValid(self, s: str) -> bool:
        if not s:
            return True

        i = 0
        while i < len(s):
            looking_for_partner = s[i]
            if looking_for_partner not in self.partner_table:
                return False
            partner = self.partner_table[looking_for_partner]

            j = i + 1
            depth = 1
            while depth > 0:
                if j >= len(s):
                    return False
                if s[j] == looking_for_partner:
                    depth += 1
                if s[j] == partner:
                    depth -= 1
                j += 1

            if not self.isValid(s[i+1:j-1]):
                return False

            i = j

        return True


if __name__ == '__main__':
    print(Solution().isValid("{}{}()[]"))