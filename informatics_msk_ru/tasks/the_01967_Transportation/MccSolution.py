import os
import sys
from collections import defaultdict
from heapq import heappop, heappush

MX_T = 1440
EMPTY_TRUCK_W = 3000000


def check(N, adj, edge_info, weight):
    dp = [MX_T + 1] * (N + 1)
    dp[1] = 0
    q = [(0, 1)]

    while q:
        u_t, u = heappop(q)
        if u_t > dp[u]:
            continue

        dp[u] = u_t

        for v in adj[u]:
            u_v_t, v_max_weight = edge_info.get((u, v), None) or edge_info[(v, u)]
            if v_max_weight < weight + EMPTY_TRUCK_W:
                continue

            v_t = u_t + u_v_t
            if v_t >= dp[v] or v_t > MX_T:
                continue

            if v == N:
                return True

            dp[v] = v_t
            heappush(q, (v_t, v))

    return False


def solution(N, es):
    if N == 1:
        return 10000000

    adj = defaultdict(list)
    edge_info = {}

    for u, v, t, max_weight in es:
        adj[u].append(v)
        adj[v].append(u)
        edge_info[(u, v)] = (t, max_weight)

    i, j = -1, 10000001
    while i < j - 1:
        m = i + (j - i) // 2
        if check(N, adj, edge_info, m * 100):
            i = m
        else:
            j = m

    return i if i > -1 else 0


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        N, M = map(int, next(iff).strip().split())

        # edges = (list(map(int, next(iff).strip().split())) for _ in range(M))

        def edge_producer():
            for _ in range(M):
                yield map(int, next(iff).strip().split())        

        off.write('%d' % solution(N, edge_producer()))


    parse_and_run()
