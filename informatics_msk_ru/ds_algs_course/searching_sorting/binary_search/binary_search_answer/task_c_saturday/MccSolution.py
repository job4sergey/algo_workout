import os
import sys


def check(hs, R, C, h):
    i = 0
    while R > 0 and i < len(hs) - C + 1:
        if hs[i + C - 1] - hs[i] <= h:
            R -= 1
            i += C
        else:
            i += 1

    return R == 0


def solution(N, R, C, hs):
    hs.sort()

    # i, j = hs[1] - hs[0] - 1, hs[-1] - hs[0] + 1
    i, j = -1, hs[len(hs) - 1] + 1

    while i < j - 1:
        m = i + (j - i) // 2
        if check(hs, R, C, m):
            j = m
        else:
            i = m

    return j


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout
        N, R, C = map(int, next(iff).strip().split())
        hs = [int(next(iff).strip()) for _ in range(N)]
        off.write('%d' % solution(N, R, C, hs))


    parse_and_run()
