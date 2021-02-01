def swap(a, minx, i):
    a[minx], a[i] = a[i], a[minx]
    return a


"""
At the start of each ("i"th) iteration the "i"th element is considered as the minimum.
After "i"th iteration the smallest element(found by comparing "i"th element with remaining elements) 
is bought to the corresponding "i"th position 
"""


def selectionsort(a):
    n = len(a)
    for i in range(0, n - 1):
        minx = i
        for k in range(i + 1, n):
            if a[k] < a[minx]:
                minx = k

        a = swap(a, minx, i)

    return a


a = [5, 4, 2, 7, 5, 2, 10, 12, 14, 23, 17]
print("Unsorted array = {}".format(a))
print("Sorted array = {}".format(selectionsort(a)))
