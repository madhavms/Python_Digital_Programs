"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.



Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"

"""

import math


def getPermutation(n, k):
    nums = list(range(1, n + 1))
    out = ''

    while n > 1:
        temp = math.factorial(n - 1)
        pos = (k - 1) // temp
        k = k % temp
        nn = nums[pos]
        out += str(nn)
        nums.remove(nn)
        n -= 1

    return out + str(nums[-1])


n = [3, 4, 3]
k = [3, 9, 1]

for i in range(3):
    print("n= {} , k = {}".format(n[i], k[i]))
    print(getPermutation(n[i], k[i]))
    print()
