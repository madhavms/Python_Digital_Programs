"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1
"""

# Consider s = "aeiouaeiou"


def maxVowels(s, k):
    ans = 0
    out = 0
    vow = 'aeiou'

    # find the number of vowels in first substring
    for i in range(0,k):
        if(s[i] in vow):
            ans += 1
    out = ans
    # now consider the remaining string
    for i in range(k,len(s)):
        # on moving to next letter if there is a vowel increase 1
        # we already have vowel count for first substring 'ae'
        # on iterating 'ae' -> 'ei' add count for 'i' and reduce count for 'a'
        # continue this process
        if(s[i] in vow):
            ans+=1

        if(s[i-k] in vow):
            ans-=1

        out = max(out,ans)

    return out




    

a = "aeiouaeiou"


print(maxVowels(a,2))