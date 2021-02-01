# youtube explanation link: https://www.youtube.com/watch?v=UZRkpGk943Q

def longestPalindrome(s):
    X = s
    Y = s[::-1]
    n = len(X)
    LCSuff = [[0 for k in range(n + 1)] for l in range(n + 1)]
    result = 0
    pos = 0

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1

            result = max(result, LCSuff[i][j])

            if result == LCSuff[i][j]:
                pos = i

            else:
                LCSuff[i][j] = 0

    start = pos - result
    print(start, pos, result)

    out = ''
    maxout = ''
    tempout = ''
    count = 0
    P = X[start:pos]
    print(P)
    while count < len(P):
        for i in range(count, len(P)):
            out += P[i]
            if out == out[::-1]:
                tempout = out

        maxout = maxout if len(maxout) > len(tempout) else tempout
        count += 1
        out = ''

    return maxout


X = "abbcccbbbcaaccbababcbcabca"

print(longestPalindrome(X))
