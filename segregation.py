def segregation(ls):
    zeros = []
    ones = []

    for l in ls:
        if l == 0:
            zeros.append(l)
        elif l == 1:
            ones.append(l)

    return zeros + ones


arr = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
print("Input array:{}".format(arr))
print("Output segregated array:{}".format(segregation(arr)))
