import os
import sys


# stack
def solution(s):
    st = []

    for c in s:
        if c == '(' or not st or st[-1] != '(':
            st.append(c)
        else:
            st.pop()

    return len(st)


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        off.write("%s\n" % (solution(next(iff).strip())))


    parse_and_run()
