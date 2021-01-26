import os
import sys


def solution(n):
    def gcd(x, y):
        while y:
            x, y = y, x % y

        return x

    h = n // 2

    no, de = (h - 1, h + 1) if n % 2 == 0 else (h, h + 1)

    while no > 0:
        if gcd(no, de) == 1:
            break

        no -= 1
        de += 1

    return no, de


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(int(next(iff).strip()))
    off.write('%d %d' % res)
