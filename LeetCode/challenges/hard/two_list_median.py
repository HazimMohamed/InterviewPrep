from statistics import mean
from math import floor, ceil
from typing import List, Tuple


class Solution:
    @staticmethod
    def median(l: List[int]) -> Tuple[float, int]:
        middle_ind = len(l) / 2
        if len(l) % 2 == 0:
            middle_ind = int(middle_ind)
            return mean([l[middle_ind], l[middle_ind - 1]]), middle_ind
        else:
            return l[floor(middle_ind)], floor(middle_ind)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return self.median(nums2)[0]

        if not nums2:
            return self.median(nums1)[0]

        def recurse(l1: List[int], l2: List[int], split_median: bool):
            if len(l1) == 1 or len(l2) == 1:
                return Solution.median(l1 + l2)[0]

            median1, med_ind1 = self.median(l1)
            median2, med_ind2 = self.median(l2)

            if median1 > median2:
                return recurse(l1[:med_ind1],
                               l2[med_ind2:],
                               split_median)
            else:
                return recurse(l1[med_ind1:],
                               l2[:med_ind2 + 1],
                               split_median)

        return recurse(nums1, nums2, (len(nums1) + len(nums2)) % 2 == 0)


s = Solution()
print(s.findMedianSortedArrays([1, 3, 6, 7], [2, 5, 13, 22]))
