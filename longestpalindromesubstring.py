"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
"""

def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return ""
    ml = 1  # to store value of maximum length
    st = 0  # to store starting index of the palindromic substring

    for i in range(n):
        # checking for odd length palindrome centered at index i
        begin = i
        end = i
        while begin >= 0 and end < n and s[begin] == s[end]:
            print(begin,end,s[begin],s[end],"odd")
            begin -= 1
            end += 1
            #print(begin,end)

        print("end......")
        if end - begin - 1 > ml:  # determining new max length of palindromic substring and its starting index

            ml = end - begin - 1
            st = begin + 1

        # checking for even length palindrome centered at index i and i+1
        begin = i
        end = i + 1
        while begin >= 0 and end < n and s[begin] == s[end]:
            print(begin, end, s[begin], s[end], "even")
            begin -= 1
            end += 1
        if end - begin - 1 > ml:  # determining new max length of palindromic susbtring and its starting index

            ml = end - begin - 1
            st = begin + 1

    return s[st:st + ml]




sa = "ammaachan"

print(longestPalindrome(sa))






