def array_input():
    a = []
    b = []

    m = int(input("enter no of rows: "))
    n = int(input("enter no of columns: "))

    for i in range(n):
        a = []
        print("Enter row {}".format(i+1))
        for j in range(m):
            a.append(input())
        b.append(a)
    return b, m, n


def row_sum():
    sums = []

    res = array_input()

    b = res[0]
    r = res[1]
    c = res[2]

    for i in range(0, r):
        sum_r = 0
        for j in range(0, c):
            sum_r += int(b[i][j])
        sums.append(sum_r)

    return sums


print(row_sum())
