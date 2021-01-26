import os
import sys


def solution(ns):
    def gcd(x, y):
        while y:
            x, y = y, x % y

        return x

    acc = ns[0]
    for n in ns[1:]:
        acc = gcd(acc, n)

    return acc


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    next(iff)
    res = solution(list(map(int, next(iff).strip().split())))
    off.write('%d' % res)
