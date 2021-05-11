import os
import sys
from collections import deque


def solution(N, src, dst):
    if src == dst:
        return [src]

    par = {src: None}

    q = deque([src])
    while q:
        u = q.popleft()

        difs = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        x, y = u
        for dx, dy in difs:
            x2, y2 = x + dx, y + dy
            v = (x2, y2)
            if x2 < 1 or x2 > N or y2 < 1 or y2 > N or v in par:
                continue

            par[v] = u
            if v == dst:
                q.clear()
                break

            q.append(v)

    if dst not in par:
        return None

    res = []
    v = dst
    while v in par:
        res.append(v)
        v = par[v]

    res.reverse()
    return res


def parse_and_run(iff, off):
    N, = map(int, next(iff).strip().split())
    x1, y1 = map(int, next(iff).strip().split())
    x2, y2 = map(int, next(iff).strip().split())
    res = solution(N, (x1, y1), (x2, y2))
    off.write('%d\n' % (len(res) - 1))

    for u in res:
        off.write('%d %d\n' % u)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
