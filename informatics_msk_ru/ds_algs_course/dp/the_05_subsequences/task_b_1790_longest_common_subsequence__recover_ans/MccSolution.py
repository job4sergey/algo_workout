import os
import sys


def solution(a1, a2):
    sz1, sz2 = len(a1), len(a2)

    dp = [[0] * (sz2 + 1) for _ in range(sz1 + 1)]

    for i in range(1, sz1 + 1):
        for j in range(1, sz2 + 1):
            if a1[i - 1] == a2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

    res = []
    i, j = sz1, sz2

    while i and j:
        if a1[i - 1] == a2[j - 1]:
            res.append(a1[i - 1])
            if dp[i][j] == 1 + dp[i - 1][j - 1]:
                i -= 1
                j -= 1
                continue

        if dp[i][j] == dp[i - 1][j]:
            i -= 1
            continue

        j -= 1

    return reversed(res)


def parse_and_run(iff):
    next(iff)
    a1 = list(map(int, next(iff).strip().split()))
    next(iff)
    a2 = list(map(int, next(iff).strip().split()))

    return solution(a1, a2)


if 'NOMAIN' not in os.environ:
    off = sys.stdout
    off.write('%s' % (' '.join(map(str, parse_and_run(sys.stdin)))))
