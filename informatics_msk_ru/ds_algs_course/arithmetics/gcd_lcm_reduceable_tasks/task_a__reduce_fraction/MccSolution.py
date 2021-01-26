import os
import sys


def solution(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y

        return x

    g = gcd(a, b)
    return a // g, b // g


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(*map(int, next(iff).strip().split()))
    off.write('%d %d' % res)
