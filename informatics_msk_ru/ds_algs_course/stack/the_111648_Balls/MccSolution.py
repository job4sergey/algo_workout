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


def solution(balls):
    st = []
    res = 0

    for b in balls:
        if not st:
            st.append([b, 1])
            continue

        if st[-1][0] == b:
            st[-1][1] += 1
        else:
            res += reduce_top(st)
            if not st:
                st.append([b, 1])
                continue

            if st[-1][0] == b:
                st[-1][1] += 1
            else:
                st.append([b, 1])

    res += reduce_top(st)
    st.clear()
    return res


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        ns = list(map(int, next(iff).strip().split()))
        res = solution(ns[1:])
        off.write("%s\n" % res)


    parse_and_run()
