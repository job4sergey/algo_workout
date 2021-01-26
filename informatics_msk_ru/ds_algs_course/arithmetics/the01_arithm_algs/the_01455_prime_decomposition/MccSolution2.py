import os
import sys

# prime factorization
# prime decomposition
def solution(n0):
    def factor(p, cn):
        return '%s^%s' % (p, cn) if cn > 1 else str(p)

    def run(n):
        res = []

        cn = 0
        while n % 2 == 0:  # we eliminate all 2s because all primes except 2 are odd
            cn += 1
            n >>= 1

        if cn:
            res.append(factor(2, cn))

        p = 3
        # if n is composite -> it has prime divisor <= to sqrt(n)
        while p * p <= n:
            cn = 0
            while n % p == 0:
                n //= p
                cn += 1

            if cn:
                res.append(factor(p, cn))

            p += 2

        if n > 2:  # n is prime
            res.append(factor(n, 1))

        return '*'.join(res)

    return run(n0)


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    off.write('%s' % solution(int(next(iff))))
