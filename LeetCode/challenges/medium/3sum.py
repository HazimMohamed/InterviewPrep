from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_sums = set({})
        seen = {nums[0]}
        for elem in nums[1:]:
            goal = target - elem
            if goal in seen:
                to_add = (elem, goal) if goal < elem else (goal, elem)
                all_sums.add(to_add)
            seen.add(elem)

        return list(all_sums)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = []

        been_popped = set({})
        for i in range(len(nums)):
            popped_elem = nums[i]
            if popped_elem not in been_popped:
                been_popped.add(popped_elem)
                popped_list = nums[:i] + nums[i + 1:]
                looking_for_sum = -1 * popped_elem

                possible_sums = self.twoSum(popped_list, looking_for_sum)

                for possible_sum in possible_sums:
                    solution_set.append(sorted([popped_elem, *possible_sum]))

        return [solution for ind, solution in enumerate(solution_set) if solution not in solution_set[ind+1:]]


if __name__ == '__main__':
    print(Solution().threeSum( [-1, 0, 1, 2, -1, -4] ))