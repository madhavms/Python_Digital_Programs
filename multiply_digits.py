"""
Input a number and multiply the digits and return the result

Input: 12345
Output: 1*2*3*4*5 = 120

Constraint: 0<n<10000
"""


def multiply_digits(n):
    # constraint
    if not 0 < n <= 10000:
        return
    mult = 1
    for i in str(n):
        mult *= int(i)
    return mult


N = int(input("Enter the number:"))
print("The output is:{}".format(multiply_digits(N)))
