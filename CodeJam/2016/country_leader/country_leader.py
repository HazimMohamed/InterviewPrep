def solve(list_names):
    greatest_leaders = []
    max_characters = 0
    for name in list_names:
        chars_in_name = len(list(filter(lambda a: a != ' ', set(list(name)))))
        if chars_in_name > max_characters:
            max_characters = chars_in_name
            greatest_leaders = [name]
        elif chars_in_name == max_characters:
            greatest_leaders.append(name)
    greatest_leaders.sort()
    return greatest_leaders[0]


num_test_cases = int(input())
for i in range(num_test_cases):
    num_names = int(input())
    name_list = []
    for j in range(num_names):
        name_list.append(input())
    print('Case #{}: {}'.format(i+1, solve(name_list)))