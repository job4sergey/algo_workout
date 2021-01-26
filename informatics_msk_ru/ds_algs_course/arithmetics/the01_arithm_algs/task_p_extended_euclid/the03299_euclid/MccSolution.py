import os
import sys


# extended euclid

def gcde(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = gcde(b, a % b)
    return g, y1, x1 - (a // b) * y1


def solution(a, b, c):
    g, x, y = gcde(abs(a), abs(b))
    if c % g != 0:
        return None

    x *= c // g
    y *= c // g

    if a < 0:
        x *= -1

    if b < 0:
        y *= -1

    return g, x, y


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    res = solution(*map(int, next(iff).strip().split()))
    off.write('%s' % (' '.join(map(str, res)) if res else 'Impossible'))
