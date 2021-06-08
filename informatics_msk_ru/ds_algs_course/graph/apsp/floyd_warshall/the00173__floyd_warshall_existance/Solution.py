import os
import sys


def solution(D):
    N = len(D)

    for r in range(N):
        for c in range(N):
            if D[r][c] == 0:
                D[r][c] = float('inf') if r != c else 0

    for k in range(N):
        for r in range(N):
            for c in range(N):
                if D[r][c] > D[r][k] + D[k][c]:
                    D[r][c] = D[r][k] + D[k][c]

    res = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if D[r][c] == float('inf'):
                res[r][c] = 0
                continue

            res[r][c] = 1
            for k in range(N):
                if D[r][k] != float('inf') and D[k][k] < 0 and D[k][c] != float('inf'):
                    res[r][c] = 2
                    break

    return res


def parse_and_run(iff, off):
    N, = map(int, next(iff).strip().split())

    madj = []
    for u in range(N):
        madj.append(list(map(int, next(iff).strip().split())))

    res = solution(madj)
    for row in res:
        off.write('%s\n' % (' '.join(map(str, row))))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
