# a = input('Enter the count of values you are going to insert')
# r = []
# print('Enter 5 numbers')
# for i in range(0,a):
#     b = input()
#     r.append(b)

a = 5
r = [10, 3, 5, 6, 20]


def maxquadruplet(count, numbers):
    num = 1
    if count < 4:
        return 'Invalid Input'

    numbers = sorted(numbers, reverse=True)
    for i in range(4):
        num *= numbers[i]
    print(numbers)
    return num


print(maxquadruplet(a, r))
