import os
import sys


# stack
def solution(cs):
    res = [float('-inf')]
    st = []

    for c in cs:
        while st and st[-1] < c:
            c0 = st.pop()
            if res[-1] > c0:
                return 0

            res.append(c0)

        st.append(c)

    while st:
        c0 = st.pop()
        if res[-1] > c0:
            return 0

        res.append(c0)

    return 1


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        N = int(next(iff).strip())

        for _ in range(N):
            cs = list(map(float, next(iff).strip().split()))[1:]
            res = solution(cs)
            off.write("%s\n" % res)


    parse_and_run()
