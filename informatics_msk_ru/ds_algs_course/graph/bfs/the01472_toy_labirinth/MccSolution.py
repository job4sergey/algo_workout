import os
import sys
from collections import deque


def solution(gd):
    rc, cc = len(gd), len(gd[0])

    LEFT = [[0] * cc for _ in range(rc)]  # column to stop when moving left

    for r in range(rc):
        for c in range(cc):
            if gd[r][c] == 1:
                LEFT[r][c] = c + 1
                continue
            elif gd[r][c] == 2:
                LEFT[r][c] = c
                continue

            LEFT[r][c] = LEFT[r][c - 1] if c > 0 else 0

    RIGHT = [[cc - 1] * cc for _ in range(rc)]  # column to stop when moving right
    for r in range(rc):
        for c in range(cc - 1, -1, -1):
            if gd[r][c] == 1:
                RIGHT[r][c] = c - 1
                continue
            elif gd[r][c] == 2:
                RIGHT[r][c] = c
                continue

            RIGHT[r][c] = RIGHT[r][c + 1] if c < cc - 1 else cc - 1

    UP = [[0] * cc for _ in range(rc)]  # row to stop when moving up
    for r in range(rc):
        for c in range(cc):
            if gd[r][c] == 1:
                UP[r][c] = r + 1
                continue
            elif gd[r][c] == 2:
                UP[r][c] = r
                continue

            UP[r][c] = UP[r - 1][c] if r > 0 else 0

    DOWN = [[rc - 1] * cc for _ in range(rc)]  # row to stop when moving down
    for r in range(rc - 1, -1, -1):
        for c in range(cc):
            if gd[r][c] == 1:
                DOWN[r][c] = r - 1
                continue
            elif gd[r][c] == 2:
                DOWN[r][c] = r
                continue

            DOWN[r][c] = DOWN[r + 1][c] if r < rc - 1 else rc - 1

    vis = {(0, 0)}
    q = deque([(0, 0, 0)])
    while q:
        r, c, cn = q.popleft()

        for c2 in (LEFT[r][c], RIGHT[r][c]):
            if (r, c2) not in vis:
                if gd[r][c2] == 2:
                    return cn + 1

                vis.add((r, c2))
                q.append((r, c2, cn + 1))

        for r2 in (UP[r][c], DOWN[r][c]):
            if (r2, c) not in vis:
                if gd[r2][c] == 2:
                    return cn + 1

                vis.add((r2, c))
                q.append((r2, c, cn + 1))

    return -1


def parse_and_run(iff, off):
    rc, cc = map(int, next(iff).strip().split())

    gd = []

    for u in range(rc):
        gd.append(list(map(int, next(iff).strip().split())))

    off.write('%d' % solution(gd))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
