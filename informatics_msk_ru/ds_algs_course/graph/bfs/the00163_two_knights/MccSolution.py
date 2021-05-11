import os
import sys
from collections import deque


def solution(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0

    SZ = 8

    vis = [
        [
            [
                [0] * SZ for _ in range(SZ)
            ] for _ in range(SZ)
        ] for _ in range(SZ)
    ]

    vis[r1][c1][r2][c2] = 1

    q = deque([(r1, c1, r2, c2, 0)])

    #     (-2, -1)	(-2 ,1)
    # (-1 ,-2)				(-1 ,2)
    # (1 ,-2)				(1 ,2)
    # (2 ,-1)		(2 ,1)

    difs = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    while q:
        r1, c1, r2, c2, cn = q.popleft()
        for dr1, dc1 in difs:
            for dr2, dc2 in difs:
                r1n, c1n, r2n, c2n = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                if r1n < 0 or r1n > SZ - 1 or \
                        c1n < 0 or c1n > SZ - 1 or \
                        r2n < 0 or r2n > SZ - 1 or \
                        c2n < 0 or c2n > SZ - 1 or \
                        vis[r1n][c1n][r2n][c2n]:
                    continue

                if r1n == r2n and c1n == c2n:
                    return cn + 1

                vis[r1n][c1n][r2n][c2n] = 1
                q.append((r1n, c1n, r2n, c2n, cn + 1))

    return -1


def parse_and_run(iff, off):
    css1, css2 = next(iff).strip().split()

    r1 = ord(css1[0]) - ord('a')
    r2 = ord(css2[0]) - ord('a')
    c1 = ord(css1[1]) - ord('1')
    c2 = ord(css2[1]) - ord('1')

    off.write('%s\n' % solution(r1, c1, r2, c2))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
