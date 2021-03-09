import os
import sys


def parse_and_run(iff):
    _, k = map(int, next(iff).strip().split())
    return solution(next(iff).strip(), k)


# TLE
def solution(s, K):
    sz = len(s)
    cn = 0

    for k in range(sz):
        for i, j in ((k, k), (k - 1, k)):
            is_poly = 1
            budg = K
            while i > -1 and j < sz and is_poly:
                is_poly = s[i] == s[j]
                if not is_poly:
                    budg -= 1
                    if budg < 0:
                        break
                    is_poly = 1

                cn += is_poly
                i -= 1
                j += 1

    return cn


if 'NOMAIN' not in os.environ:
    off = sys.stdout
    off.write('%s' % parse_and_run(sys.stdin))
