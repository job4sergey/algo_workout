import os
import sys


def solution(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y

        return x

    de, no = a * d + b * c, b * d
    g = gcd(de, no)
    return de // g, no // g


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(*map(int, next(iff).strip().split()))
    off.write('%d %d' % res)
