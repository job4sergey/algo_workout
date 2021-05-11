import os
import sys
from collections import deque


def solution(gd, x1, y1, x2, y2):
    rc, cc = len(gd), len(gd[0])
    q = deque()

    def cost(x, y):
        return 2 if gd[x][y] == 'W' else 1

    vis = set()

    def enq(x, y, hs, dir, dur):
        if x < 0 or x == rc or y < 0 or y == cc or gd[x][y] == '#' or (x, y) in vis:
            return None

        vis.add((x, y))
        tm = cost(x, y)

        if x == x2 and y == y2:
            return dur + tm, hs + dir

        q.append((x, y, tm - 1, hs + dir, dur + tm))

        return None

    def main():
        if enq(x1, y1, '', '', -cost(x1, y1)):
            return 0, []

        res = None
        while q:
            x, y, tm, hs, dur = q.popleft()
            if tm > 0:
                q.append((x, y, tm - 1, hs, dur))
                continue

            res = enq(x + 1, y, hs, 'S', dur) or \
                  enq(x - 1, y, hs, 'N', dur) or \
                  enq(x, y - 1, hs, 'W', dur) or \
                  enq(x, y + 1, hs, 'E', dur)
            if res:
                break

        return res

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
        off.write("%s" % hs)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
