import os
import sys


def solution(D, u0, v0):
    N = len(D)

    D0 = [[0] * N for _ in range(N)]
    P = [[-1] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            D0[r][c] = D[r][c]

    for k in range(N):
        for r in range(N):
            for c in range(N):
                if D[r][c] > D[r][k] + D[k][c]:
                    D[r][c] = D[r][k] + D[k][c]
                    P[r][c] = k

    if D[u0][v0] == float('inf'):
        return 0

    def rec(u, v):
        if P[u][v] == -1:
            return []

        return rec(u, P[u][v]) + [P[u][v]] + rec(P[u][v], v)

    path = [u0] + rec(u0, v0) + [v0]
    res = 1.0
    for v in range(1, len(path)):
        res *= (100.0 - D0[path[v - 1]][path[v]]) / 100.0

    return 1.0 - res


def parse_and_run(iff, off):
    N, M = map(int, next(iff).strip().split())
    u0, v0 = map(int, next(iff).strip().split())

    madj = [[float('inf')] * N for _ in range(N)]

    for u in range(N):
        madj[u][u] = 0

    for _ in range(M):
        u, v, w = map(int, next(iff).strip().split())
        madj[u - 1][v - 1] = w
        madj[v - 1][u - 1] = w

    res = solution(madj, u0 - 1, v0 - 1)
    off.write('%s\n' % res)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
