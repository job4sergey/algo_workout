import os
import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(N, adj, u0, v0):
    if u0 == v0:
        return [u0]

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
        return None

    v = v0
    res = []
    while v is not None:
        res.append(v + 1)
        v = par[v]

    res.reverse()

    return res


def parse_and_run(iff, off):
    N, u0, v0 = map(int, next(iff).strip().split())

    adj = defaultdict(list)
    for u in range(N):
        vs = list(map(int, next(iff).strip().split()))
        for v in range(0, len(vs)):
            if vs[v] >= 0:
                adj[u].append((v, vs[v]))

    res = solution(N, adj, u0 - 1, v0 - 1)
    if res is None:
        off.write('-1')
    else:
        off.write('%s' % ' '.join(map(str, res)))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
