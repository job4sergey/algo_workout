import os
import sys
from heapq import *


def solution(gd, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0, []

    rc, cc = len(gd), len(gd[0])

    dp = {(x1, y1): 0}

    q = []
    heappush(q, (0, x1, y1))

    pos2par = {}

    def enq(x0, y0, d0, x, y):
        if x < 0 or x == rc or y < 0 or y == cc or gd[x][y] == '#':
            return

        cst = d0 + (2 if gd[x][y] == 'W' else 1)
        if dp.get((x, y), float('inf')) <= cst:
            return

        dp[(x, y)] = cst
        pos2par[(x, y)] = (x0, y0)

        heappush(q, (cst, x, y))

    def main():
        while q:
            d, x, y = heappop(q)

            enq(x, y, d, x + 1, y)
            enq(x, y, d, x - 1, y)
            enq(x, y, d, x, y - 1)
            enq(x, y, d, x, y + 1)

        pos = (x2, y2)
        if pos not in pos2par:
            return None

        hs = []
        while pos:
            x, y = pos
            pos = pos2par.get(pos, None)
            if pos:
                x0, y0 = pos
                hs.append(
                    ('S' if x0 + 1 == x else None) or
                    ('N' if x0 - 1 == x else None) or
                    ('E' if y0 + 1 == y else None) or
                    ('W' if y0 - 1 == y else None)
                )

        hs.reverse()
        return dp[(x2, y2)], hs

    return main()


def parse_and_run(iff, off):
    rc, cc, x1, y1, x2, y2 = map(int, next(iff).strip().split())

    gd = []

    for u in range(rc):
        gd.append(next(iff).strip())

    res = solution(gd, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
    if res is None:
        off.write('-1')
    else:
        dur, hs = res
        off.write("%d\n" % dur)
        off.write("%s" % ''.join(hs))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
