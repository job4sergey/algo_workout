import os
import sys
from collections import deque


def solution(s1, s2):
    def to_ns(s):
        return [ord(c) - ord('0') for c in s]

    SZ = 4
    src, dst = to_ns(s1), to_ns(s2)
    if src == dst:
        return [src]

    vis = {tuple(src)}
    q = deque([(src, [])])

    def incr0(ns, is_rev=0):
        ns2 = ns + []
        ns2[0] += -1 if is_rev else 1
        return ns2

    def decrX(ns, is_rev=0):
        ns2 = ns + []
        ns2[SZ - 1] += 1 if is_rev else -1
        return ns2

    def rotate(ns, is_left):
        return ns[1:] + [ns[0]] if is_left else [ns[-1]] + ns[:-1]

    INC0 = 0
    DECX = 3
    ROTL = 4
    ROTR = 5

    is_found = False
    while q:
        u, acts = q.popleft()

        for what in (INC0, DECX, ROTL, ROTR):
            v = None
            if what == INC0:
                if u[0] < 9:
                    v = incr0(u)
            elif what == DECX:
                if u[SZ - 1] > 1:
                    v = decrX(u)
            else:
                v = rotate(u, is_left=what == ROTL)

            if v:
                vt = tuple(v)
                if vt in vis:
                    continue

                if v == dst:
                    is_found = True
                    acts = acts + [what]
                    q.clear()
                    break

                vis.add(vt)
                q.append((v, acts + [what]))

    if is_found:
        res = [dst]
        u = dst

        while acts:
            what = acts.pop()
            if what == INC0:
                u = incr0(u, is_rev=True)
            elif what == DECX:
                u = decrX(u, is_rev=True)
            else:
                u = rotate(u, is_left=what == ROTR)
            res.append(u)

        res.reverse()
        return res

    return []


def parse_and_run(iff, off):
    s1 = next(iff).strip()
    s2 = next(iff).strip()

    res = solution(s1, s2)
    for ns in res:
        off.write('%s\n' % ''.join(map(str, ns)))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
