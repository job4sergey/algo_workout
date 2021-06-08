import os
import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(adj, madj, u0, v0):
    dp = {u0: 0}
    par = {u0: None}
    q = [(0, u0)]
    while q:
        d, u = heappop(q)
        for v, w in adj[u]:
            if d + w >= dp.get(v, float('inf')):
                continue

            dp[v] = d + w
            par[v] = u
            heappush(q, (d + w, v))

    if dp.get(v0, None) is None:
        return 0

    v = v0
    res = []
    while v is not None:
        res.append(v)
        v = par[v]

    res.reverse()

    prob = 1.0
    for u in range(1, len(res)):
        prob *= (100.0 - madj[res[u - 1]][res[u]]) / 100.0

    return 1.0 - prob


def parse_and_run(iff, off):
    adj = defaultdict(list)
    N, M = map(int, next(iff).strip().split())
    u0, v0 = map(int, next(iff).strip().split())

    madj = [[float('inf')] * N for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, next(iff).strip().split())
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))
        madj[u - 1][v - 1] = w
        madj[v - 1][u - 1] = w

    res = solution(adj, madj, u0 - 1, v0 - 1)
    off.write('%s\n' % res)


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
