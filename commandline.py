import sys

s = sys.argv
n = len(s)

print("Total length of arguments = {}".format(n))

print("Name of python script = {}".format(s[0]))

print("Arguments passed :", end=" ")

for i in range(1, n):
    print(s[i], end=" ")

sum_var = 0

for i in range(1, n):
    sum_var += int(sys.argv[i])

print("\nSum = {}".format(sum_var))
