import os
import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(cs, adj):
    u0, v0 = 0, len(cs) - 1
    if u0 == v0:
        return 0

    dp = {u0: 0}
    q = [(0, u0)]
    while q:
        d, u = heappop(q)
        w = cs[u]
        for v in adj[u]:
            if d + w >= dp.get(v, float('inf')):
                continue

            dp[v] = d + w
            heappush(q, (d + w, v))

    if dp.get(v0, None) is None:
        return -1

    return dp[v0]


def parse_and_run(iff, off):
    _, = map(int, next(iff).strip().split())
    cs = list(map(int, next(iff).strip().split()))

    N, = map(int, next(iff).strip().split())

    adj = defaultdict(list)
    for u in range(N):
        u, v = list(map(int, next(iff).strip().split()))
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    res = solution(cs, adj)
    off.write('%d' % res)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
