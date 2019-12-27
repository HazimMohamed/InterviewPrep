def solve(total):
    k = 2
    a, b = total, 0
    while contains_4(a) or contains_4(b):
        if a == 0 or b == 0:
            a, b = total, 0
            k += 1
        a = a // k
        b = total - a

    return a, b


def contains_4(num):
    return str(num).__contains__('4')


test_cases = int(input())

for i in range(test_cases):
    num = int(input())
    print("Case #{}: {} {}".format(i + 1, *solve(num)))
