import os
import sys


# find leftmost element, which is greater or equal to x
def bs_ge(a, i, x):
    j = len(a)

    while i < j - 1:
        m = i + (j - i) // 2
        if a[m] < x:
            i = m
        else:
            j = m

    return j


def check(a, dist, n_cows):
    i = 0
    # cows > 0 -> we still has some cows to place
    # n_cows <= len(a) - i -> we still have enough space to place all the cows
    while 0 < n_cows <= len(a) - i:
        n_cows -= 1
        i = bs_ge(a, i, a[i] + dist)

    return n_cows == 0


def solution(n_cows, stables):
    if n_cows > len(stables):
        return 0

    i, j = -1, stables[len(stables) - 1] - stables[0] + 1

    # find the righmost value of distance,
    # s.t. it is still possible to have this as min dist between cows
    while i < j - 1:
        m = i + (j - i) // 2
        if check(stables, m, n_cows):
            i = m
        else:
            j = m

    return i


if 'NOMAIN' not in os.environ:
    iff, off = sys.stdin, sys.stdout
    n_cows = list(map(int, next(iff).strip().split()))[1]
    stables = list(map(int, next(iff).strip().split()))
    res = solution(n_cows, stables)
    off.write('%d' % res)
