import os
import sys
from collections import deque


def solution(gd):
    fro, to = None, None
    rc, cc = len(gd), len(gd[0])

    for r in range(1, rc - 1):
        if fro and to:
            break
        for c in range(1, cc - 1):
            if gd[r][c] == 'S':
                fro = (r, c)
            elif gd[r][c] == 'F':
                to = (r, c)

            if fro and to:
                break

    # all directions in clockwise order
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    # initially we can choose whatever direction we prefer
    q = deque([(fro[0], fro[1], i, 0) for i in range(len(dirs))])

    vis = {}  # coord to direction mapping
    # we consider the coord visited iff we have visited it with the same direction

    for i in range(len(dirs)):
        vis[(fro[0], fro[1])] = i

    # path = {}

    while q:
        r, c, cur_dir_i, cn = q.popleft()
        # path[(r, c)] = cn

        for i in (cur_dir_i, (cur_dir_i + 1) % len(dirs)):
            dr, dc = dirs[i]
            r2, c2 = r + dr, c + dc

            if vis.get((r2, c2), -1) == i or gd[r2][c2] == 'X':
                continue

            if r2 == to[0] and c2 == to[1]:
                return cn + 1

            vis[(r2, c2)] = i
            q.append((r2, c2, i, cn + 1))

    # for r in range(0, rc):
    #     for c in range(0, cc):  # and (r, c) not in (fro, to)
    #         if (r, c) in path:
    #             print('.', end='')
    #         else:
    #             print(gd[r][c], end='')
    #     print()

    return -1


def parse_and_run(iff, off):
    rc, cc = map(int, next(iff).strip().split())

    gd = []

    for u in range(rc):
        gd.append(next(iff).strip())

    off.write('%d' % solution(gd))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
