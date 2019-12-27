from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        common_prefix = ''
        all_same = True
        while all_same:
            ind = len(common_prefix)
            if ind < len(strs[0]):
                common_letter = strs[0][ind]
                for elem in strs:
                    if ind >= len(elem) or elem[ind] != common_letter:
                        all_same = False
                if all_same:
                    common_prefix += common_letter
            else:
                all_same = False
        return common_prefix