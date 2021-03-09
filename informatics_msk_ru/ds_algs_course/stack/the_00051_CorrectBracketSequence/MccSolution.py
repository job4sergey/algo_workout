import os
import sys


# stack
def solution(s):
    st = []
    b2b = {'}': '{', ']': '[', ')': '('}

    for c in s:
        if st and st[-1] == b2b.get(c):
            st.pop()
        else:
            st.append(c)

    return not st


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        res = solution(next(iff).strip())
        off.write("yes" if res else "no")


    parse_and_run()
