"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""
def longestUniqueSubsttr(string):
    seen = {}
    max_length = 0
    start = 0

    for end, c in enumerate(string):

        if c in seen:
            start = max(start, seen[c] + 1)

        seen[c] = end
        max_length = max(max_length, end - start + 1)

    return max_length


a = "abcabcbb"

print(longestUniqueSubsttr(a))
