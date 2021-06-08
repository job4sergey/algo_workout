import os
import sys


def solution(D):
    N = len(D)

    for r in range(N):
        for c in range(N):
            if D[r][c] < 0:
                D[r][c] = float('inf') if r != c else 0

    for k in range(N):
        for r in range(N):
            for c in range(N):
                if D[r][c] > D[r][k] + D[k][c]:
                    D[r][c] = D[r][k] + D[k][c]

    mx = 0

    for r in range(N):
        for c in range(N):
            if D[r][c] != float('inf'):
                mx = max(mx, D[r][c])

    return mx


def parse_and_run(iff, off):
    N, = map(int, next(iff).strip().split())

    madj = []
    for u in range(N):
        madj.append(list(map(int, next(iff).strip().split())))

    res = solution(madj)
    off.write('%s\n' % res)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
