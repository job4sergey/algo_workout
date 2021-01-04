import os
import sys


def solution(N, x, y):
    if x > y:
        x, y = y, x

    def check(t, n):
        # t -= x
        # n -= 1
        #
        # if t < 0:
        #     return False
        # elif n == 0:
        #     return True
        #
        # return n <= t // x + t // y

        return n - 1 <= (t - x) // x + (t - x) // y

    i, j = 0, N * y

    while i < j - 1:
        m = i + (j - i) // 2
        if not check(m, N):
            i = m
        else:
            j = m

    return j


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(*list(map(int, next(iff).strip().split())))
    off.write('%d' % res)
