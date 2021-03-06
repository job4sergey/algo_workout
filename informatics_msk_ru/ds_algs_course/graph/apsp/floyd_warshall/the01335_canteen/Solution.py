import os
import sys


def solution(D):
    N = len(D)

    for k in range(N):
        for r in range(N):
            for c in range(N):
                if D[r][c] > D[r][k] + D[k][c]:
                    D[r][c] = D[r][k] + D[k][c]

    mn = (float('inf'), float('inf'))

    for r in range(N):
        mx = 0
        for c in range(N):
            if r == c:
                continue
            mx = max(mx, D[r][c])
        mn = min(mn, (mx, r))

    return mn[1]


def parse_and_run(iff, off):
    N, M = map(int, next(iff).strip().split())

    madj = [[float('inf')] * N for _ in range(N)]

    for u in range(N):
        madj[u][u] = 0

    for _ in range(M):
        u, v, l = map(int, next(iff).strip().split())
        madj[u - 1][v - 1] = l
        madj[v - 1][u - 1] = l

    res = solution(madj)
    off.write('%s\n' % (res + 1))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
