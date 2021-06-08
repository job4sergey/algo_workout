import os
import sys


def solution(D):
    N = len(D)

    for k in range(N):
        for r in range(N):
            for c in range(N):
                if D[r][c] > D[r][k] + D[k][c]:
                    D[r][c] = D[r][k] + D[k][c]

    return D


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
