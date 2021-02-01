def binarysearch(list, target):
    list = sorted(list)
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid - 1
        else:
            return mid

    return - 1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = 3

result = binarysearch(a, b)
if result != -1:
    print("{} is present at {} index of array {}".format(b, result, a))

else:
    print("{} is not present in array {}".format(b, a))
