class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matches(s: str, p: str) -> bool:
            return p == '.' or s == p

        p_pointer = 0
        s_pointer = 0

        while s_pointer < len(s) and p_pointer < len(p):
            if (p_pointer + 1) < len(p) and p[p_pointer + 1] == '*':
                if s[s_pointer] == p[p_pointer]:
                    try:
                        while matches(s[s_pointer], p[p_pointer]):
                            s_pointer += 1
                    except IndexError:
                        return (len(s) == s_pointer) and (len(p) == p_pointer + 2)
                p_pointer += 2
            elif matches(s[s_pointer], p[p_pointer]):
                p_pointer += 1
                s_pointer += 1

        return (len(s) == s_pointer) and (len(p) == p_pointer)

print(Solution().isMatch('ab', '.*'))