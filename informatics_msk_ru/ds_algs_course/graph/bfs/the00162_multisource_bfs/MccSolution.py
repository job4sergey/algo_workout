import os
import sys
from collections import deque


def solution(gd):
    rc, cc = len(gd), len(gd[0])
    res = [[0] * cc for _ in range(rc)]

    q = deque()

    for r in range(rc):
        for c in range(cc):
            if gd[r][c] == 1:
                q.append((r, c, r, c))

    while q:
        r, c, r0, c0 = q.popleft()

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r2, c2 = r + dr, c + dc
            if r2 < 0 or r2 == rc or c2 < 0 or c2 == cc or gd[r2][c2] == 1:
                continue

            gd[r2][c2] = 1
            res[r2][c2] = abs(r2 - r0) + abs(c2 - c0)
            q.append((r2, c2, r0, c0))

    return res


def parse_and_run(iff, off):
    N, M = map(int, next(iff).strip().split())
    gd = []

    for u in range(N):
        gd.append(list(map(int, next(iff).strip().split())))

    res = solution(gd)
    for row in res:
        off.write('%s\n' % ' '.join(map(str, row)))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
