import os
import sys


def solution(s1, s2):
    sz1, sz2 = len(s1), len(s2)

    dp = [[0] * (sz2 + 1) for _ in range(sz1 + 1)]

    for r in range(sz1):
        dp[r][0] = r

    for c in range(sz2):
        dp[0][c] = c

    for i in range(1, sz1 + 1):
        for j in range(1, sz2 + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + 1 - (s1[i - 1] == s2[j - 1]), 1 + dp[i - 1][j], 1 + dp[i][j - 1])

    return dp[sz1][sz2]


def parse_and_run(iff):
    return solution(next(iff).strip(), next(iff).strip())


if 'NOMAIN' not in os.environ:
    off = sys.stdout
    off.write('%s' % parse_and_run(sys.stdin))
