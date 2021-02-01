def bubblesort(a):
    n = len(a)
    for i in range(0, n - 1):
        for k in range(0, n - i - 1):
            if a[k] > a[k + 1]:
                temp = a[k]
                a[k] = a[k + 1]
                a[k + 1] = temp

    return a


a = [5, 4, 2, 7, 5, 2, 10, 12, 14, 23, 17]
print("Unsorted array = {}".format(a))
print("Sorted array = {}".format(bubblesort(a)))
