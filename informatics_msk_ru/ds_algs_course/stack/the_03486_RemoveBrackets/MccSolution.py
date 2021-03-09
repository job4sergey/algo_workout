import os
import sys


# stack
def solution(s):
    st = []

    for c in s:
        if c == '(':
            st.append(c)
        else:
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(c)

    return len(st)


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        off.write("%s\n" % (solution(next(iff).strip())))


    parse_and_run()
