
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
"""
Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
def longest2disticnt(s):
    left = 0
    right = 0
    maxLen = 0
    map = {}

    while (right < len(s)):
        map[s[right]] = right
        # when there are 3 unique alphabets
        if len(map) == 3:
            # finds the alphabet that has occurred least recently
            smallestIndex = min(map, key=map.get)
            # left pointer is incremented to next pointer after smallest index
            left = map[smallestIndex] + 1
            # the least occurring alphabet is removed
            del map[smallestIndex]

        maxLen = max(maxLen, right - left + 1)
        right += 1

    return maxLen


print(longest2disticnt("ccaabbb"))
