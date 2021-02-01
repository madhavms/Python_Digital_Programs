"""
The program would receive three english words as input

1. These words would be read one at a time in three separate lines
2. For the first word replace all vowels with %
3. For the second word replace all consonants with #
4. For the third word all character to be converted to upper case
5. Then concatinate these words and print them

TEST CASE:
Input: "how are you"
Output: "h%wa#eYOU"
"""


def wordConverter():
    vow = "aeiou"
    one = ""
    two = ""
    a = input("Enter the first word:")
    b = input("Enter the second word:")
    c = input("Enter the third word:")

    for x, y in zip(a, b):
        if x in vow:
            one += "%"
        else:
            one += x
        if y in vow:
            two += y
        else:
            two += "#"

    c = c.upper()

    return one + two + c


print("Converted word = {}".format(wordConverter()))
