import os
import sys


def solution(s1, s2):
    sz1, sz2 = len(s1), len(s2)

    MX = 81
    dp = [[0] * (sz2 + 1) for _ in range(sz1 + 1)]

    for i in range(1, sz1 + 1):
        for j in range(1, sz2 + 1):
            dp[i][j] = MX

            if s1[i - 1] == s2[j - 1] or s1[i - 1] == '?' or s2[j - 1] == '?':
                dp[i][j] = 1 + dp[i - 1][j - 1]

            if s1[i - 1] == '*':
                dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1], dp[i - 1][j])

            if s2[j - 1] == '*':
                dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j], dp[i][j - 1])

    return dp[sz1][sz2]


def parse_and_run(iff):
    return solution(next(iff).strip(), next(iff).strip())


if 'NOMAIN' not in os.environ:
    off = sys.stdout
    off.write('%s' % parse_and_run(sys.stdin))
