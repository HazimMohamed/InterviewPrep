class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        window_width = len(s)
        i = 0
        while window_width > 1:
            while i + window_width <= len(s):
                k = s[i: i+window_width]
                if k == k[::-1]:
                    return k
                i += 1
            i = 0
            window_width -= 1
        return s[0]
