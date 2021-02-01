"""
Write a program to input a string and remove 56 and 7
and return the result

Input: Aetgs56hsh7t56
Output: Aetgshsht

"""


def remove_nums(s):
    s = s.replace("56", "")
    s = s.replace("7", "")
    return s


s = input("Enter the string:")
print("Input String is: {}".format(s))
print("Output without '56' and '7' is: {}".format(remove_nums(s)))
