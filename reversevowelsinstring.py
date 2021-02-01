"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""


def reverseVowels(s):
    vow = 'aeiouAEIOU'
    count = 0
    s = list(s)
    ls = [y for y in s if y in vow][::-1]
    for x in range(len(s)):
        if s[x] in vow:
            s[x] = ls[count]
            count += 1
    return ''.join(s)

s = "hello"
print("Original String={}".format(s))
print("After vowel reversal={}".format(reverseVowels(s)))

