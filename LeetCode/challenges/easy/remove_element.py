from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        k = len(nums) - 1
        i = 0
        while k > 0 and nums[k] == val:
            k -= 1

        while i < k:
            if nums[i] == val:
                nums[i] = nums[k]
                nums[k] = val
                while k > 0 and nums[k] == val:
                    k -= 1
            i += 1

        ret = len(nums)
        for elem in nums:
            if elem == val:
                ret -= 1

        return ret

if __name__ == '__main__':
    print(Solution().removeElement([4,2,0,2,2,1,4,4,1,4,3,2], 4))

