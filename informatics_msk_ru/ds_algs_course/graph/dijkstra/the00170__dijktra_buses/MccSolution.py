import os
import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(u0, v0, adj):
    if u0 == v0:
        return 0

    dp = {u0: 0}
    q = [(0, u0)]
    while q:
        t, u = heappop(q)
        for t0, t1, v in adj[u]:
            if t > t0 or dp.get(v, float('inf')) <= t1:
                continue

            dp[v] = t1
            heappush(q, (t1, v))

    if dp.get(v0, None) is None:
        return -1

    return dp[v0]


def parse_and_run(iff, off):
    N, = map(int, next(iff).strip().split())
    u0, v0 = map(int, next(iff).strip().split())
    rcn, = map(int, next(iff).strip().split())

    adj = defaultdict(list)
    for u in range(rcn):
        u, t0, v, t1 = map(int, next(iff).strip().split())
        adj[u - 1].append((t0, t1, v - 1))

    for u in adj.keys():
        adj[u].sort(key=lambda x: x[0])

    res = solution(u0 - 1, v0 - 1, adj)
    if res is None:
        off.write('-1')
    else:
        off.write('%s' % res)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
