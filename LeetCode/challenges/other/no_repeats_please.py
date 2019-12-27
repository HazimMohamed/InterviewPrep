from typing import List

# This is not a LeetCode problem but a similar problem kind of problem found here:
# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please


# What is this supposed to do?
# Return all possible permutation of l


def permutations(l: str) -> List[str]:
    # l = ['a', 'b', 'c', 'd']
    # 'a' + all permutations of ['b', 'c', 'd']
    # 'b' + all permutations of ['c', 'a', 'd']
    # ...
    all_perms = []

    # Base case
    if len(l) == 1:
        return [l]

    for i in range(len(l)):
        # An element that gets removed from the list
        # popped_elem = c
        popped_char = l[i]
        # The list after popped_elem is removed
        # popped_list = [b]
        popped_str = l[:i] + l[i+1:]  # Same as saying list.remove(i)

        # Recursive call
        sub_perms = permutations(popped_str)
        # Returned [[b]]

        for sub_perm in sub_perms:
            # sub_perm = [b]
            # popped_elem + sub_perm = [c, b]
            all_perms.append(popped_char + sub_perm)
    return all_perms


def has_consecutive_characters(l: str) -> bool:
    for i in range(len(l)-1):
        if l[i] == l[i + 1]:
            return True
    return False


def perm_alone(s: str):
    # Get all the permutations of s_list
    # Ex. ['a', 'b', 'c'], ['a', 'c', 'b'], ...
    perms = permutations(s)

    # Filters the list of any sublist that contain consecutive characters
    filtered_list = filter(lambda a: not has_consecutive_characters(a), perms)

    # Recombines string
    # Ex [['a', 'b'], ['b', 'a']] -> ['ab', 'ba']
    return list(filtered_list)


# boiler plate
@time_func
def main() -> int:
    print(len(perm_alone('abfdefa')))
    return 0


# boiler plate
if __name__ == '__main__':
    exit(main())
