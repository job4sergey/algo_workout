import os
import sys


def solution(s1, s2):
    sz1, sz2 = len(s1), len(s2)

    dp = [[0] * (sz2 + 1) for _ in range(sz1 + 1)]
    dp[0][0] = 1

    parent = [[0] * (sz2 + 1) for _ in range(sz1 + 1)]

    for c in range(1, sz2):
        dp[0][c] = int(dp[0][c - 1] and s2[c - 1] == '*')

    for r in range(1, sz1):
        dp[r][0] = int(dp[r - 1][0] and s1[r - 1] == '*')

    def matching_char(i, j):
        if s1[i - 1] in '*?' and s2[j - 1] in '*?':
            return 'Z'
        elif s1[i - 1] in '*?':
            return s2[j - 1]
        else:
            return s1[i - 1]

    for i in range(1, sz1 + 1):
        for j in range(1, sz2 + 1):
            if s1[i - 1] != '*' and s2[j - 1] != '*':
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == '?' or s2[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                    parent[i][j] = (i - 1, j - 1, matching_char(i, j))

            if s1[i - 1] == '*':
                dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])
                if dp[i][j] == dp[i][j - 1]:
                    parent[i][j] = (i, j - 1, matching_char(i, j))
                elif dp[i][j] == dp[i - 1][j]:
                    parent[i][j] = (i - 1, j, '')

            if s2[j - 1] == '*':
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
                if dp[i][j] == dp[i - 1][j]:
                    parent[i][j] = (i - 1, j, matching_char(i, j))
                elif dp[i][j] == dp[i][j - 1]:
                    parent[i][j] = (i, j - 1, '')

    res = []
    cur = parent[sz1][sz2]
    while cur:
        i, j, c = cur
        res.append(c)
        cur = parent[i][j]

    return ''.join(reversed(res)) if dp[i][j] else '«No solution!'


def parse_and_run(iff):
    return solution(next(iff).strip(), next(iff).strip())


if 'NOMAIN' not in os.environ:
    off = sys.stdout
    off.write('%s' % parse_and_run(sys.stdin))
