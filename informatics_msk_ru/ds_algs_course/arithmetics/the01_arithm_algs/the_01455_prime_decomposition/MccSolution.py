import os
import sys


def solution(n0):
    def factor(p, cn):
        return '%s^%s' % (p, cn) if cn > 1 else str(p)

    def run(n):
        p = 2
        cn = 0
        res = []

        # if n is composite -> it has prime divisor <= to sqrt(n)
        while p * p <= n:
            if n % p:
                if cn:
                    res.append(factor(p, cn))
                    cn = 0
                p += 1
            else:
                n = n // p
                cn += 1

        if p == n:
            cn += 1
            n = 0

        if cn:
            res.append(factor(p, cn))

        if n:
            res.append(str(n))

        return '*'.join(res)

    return run(n0)


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    off.write('%s' % solution(int(next(iff))))
