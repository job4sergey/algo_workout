import os
import sys


def solution(rc, cc):
    dp = [[0] * cc for _ in range(rc)]
    dp[0][0] = 1

    for C in range(1, rc + cc - 1):
        c = min(cc - 1, C)
        r = C - c

        while r < rc and c > -1:
            if r > 1 and c < cc - 1:
                dp[r][c] += dp[r - 2][c + 1]

            if r > 1 and c > 0:
                dp[r][c] += dp[r - 2][c - 1]

            if r > 0 and c > 1:
                dp[r][c] += dp[r - 1][c - 2]

            if r < rc - 1 and c > 1:
                dp[r][c] += dp[r + 1][c - 2]
            r += 1
            c -= 1

    return dp[rc - 1][cc - 1]


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(*map(int, next(iff).strip().split()))
    off.write('%d' % res)
