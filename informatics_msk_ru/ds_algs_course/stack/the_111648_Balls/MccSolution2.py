import os
import sys


def reduce_top(st):
    if not st:
        return 0

    if st and st[-1][1] > 2:
        res = st[-1][1]
        st.pop()
        return res

    return 0


def top(st):
    return -1 if not st else st[-1][0]


def solution(balls):
    st = []
    res = 0

    for b in balls:
        if top(st) != b:
            res += reduce_top(st)

        if top(st) != b:
            st.append([b, 1])
        else:
            st[-1][1] += 1

    res += reduce_top(st)
    return res


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        ns = list(map(int, next(iff).strip().split()))
        res = solution(ns[1:])
        off.write("%s\n" % res)


    parse_and_run()
