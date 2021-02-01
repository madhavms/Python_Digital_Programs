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
def getPermutation(self, n, k):
    def perm(num_list, num, k):
        n = len(num_list)

        if (n == 0):

            return num
        diff = math.factorial(n - 1)
        digit = (k // diff) + 1
        k = k % diff
        if not k:
            digit -= 1
        num = num * 10 + num_list[digit - 1]
        num_list.pop(digit - 1)

        return perm(num_list, num, k)

    num_list = list(range(1, n + 1))
    return perm(num_list, 0, k)




n = [3,4,3]
k = [3,9,1]

for i in range(3):
    print("n= {} , k = {}".format(n[i],k[i]))
    print(getPermutation(list(range(1, n[i] + 1)),n[i], k[i]))
    print()
