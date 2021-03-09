import os
import sys


def solution(cars):
    nxt = 1
    cn = 0
    st = []

    res = []

    for c in cars:
        cn += 1
        st.append(c)
        if st and st[-1] == nxt:
            res.append((1, cn))
            cn = 0
            while st and st[-1] == nxt:
                st.pop()
                cn += 1
                nxt += 1

            if cn:
                res.append((2, cn))
            cn = 0

    return res if not st else None


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        next(iff)

        cars = list(map(int, next(iff).strip().split()))

        res = solution(cars)
        if res:
            for act, cnt in res:
                off.write("%s %s \n" % (act, cnt))
        else:
            off.write("0 \n")


    parse_and_run()
