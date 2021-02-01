"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
"""


def removeVowels(S):
    s = 'aeiou'
    return ''.join([output for output in S if output not in s])


s = "leetcodeisacommunityforcoders"
print("original string = {}".format(s))
print("string after removing vowels = {}".format(removeVowels(s)))

