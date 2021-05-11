import os
import sys
from collections import defaultdict, deque


def solution(adj, u0, v0):
    if u0 == v0:
        return [u0]

    vis = {u0}
    par = {u0: None}

    q = deque([u0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v in vis:
                continue

            vis.add(v)
            par[v] = u

            if v == v0:
                q.clear()
                break

            q.append(v)

    if v0 not in par:
        return None

    res = []
    v = v0
    while v in par:
        res.append(v + 1)
        v = par[v]

    res.reverse()
    return res


def parse_and_run(iff, off):
    N, = map(int, next(iff).strip().split())

    i = 0
    adj = defaultdict(list)

    for u in range(N):
        vs = list(map(int, next(iff).strip().split()))
        for v in range(i, len(vs)):
            if vs[v]:
                adj[u].append(v)
                adj[v].append(u)

        i += 1

    u0, v0 = map(int, next(iff).strip().split())
    res = solution(adj, u0 - 1, v0 - 1)
    if res is not None:
        off.write('%d\n' % (len(res) - 1))
        if len(res) > 1:
            off.write('%s\n' % ' '.join(map(str, res)))
    else:
        off.write('-1\n')


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
