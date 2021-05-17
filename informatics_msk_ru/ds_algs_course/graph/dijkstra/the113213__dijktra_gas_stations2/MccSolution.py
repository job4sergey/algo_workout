import os
import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(cs, adj):
    u0, v0 = 0, len(cs) - 1
    if u0 == v0:
        return 0

    # 'two layered' graph:
    # level 0 represents state when we get to vertex with 0 fuel
    # level 1 represents state when we get to vertex with 1 fuel
    dp = [{}, {}]

    dp[0][u0] = 0
    q = [(0, u0, 0)]  # cost to get to vertex, the vertex, fuel in tank when we at vertex
    while q:
        d, u, f = heappop(q)
        cu = cs[u]  # cost at u
        cnf = []  # cost and fuel to get to v
        if f == 0:  # -1 everywhere, because 1 unit of fuel will be consumed to get to v
            cnf.append((d + cu, 1 - 1))  # buy 1 fuel
            cnf.append((d + 2 * cu, 2 - 1))  # buy 2 fuel
        elif f == 1:
            cnf.append((d, 1 - 1))  # use fuel at canister
            cnf.append((d + cu, 2 - 1))  # buy 1 extra fuel

        for v in adj[u]:
            for cv, fv in cnf:
                if cv >= dp[fv].get(v, float('inf')):
                    continue

                dp[fv][v] = cv  # we can get to 'v' with 'fv' gas in tank with 'cv' cost
                heappush(q, (cv, v, fv))

    res = min(dp[0].get(v0, float('inf')), dp[1].get(v0, float('inf')))
    if res == float('inf'):  # cannot get to v0
        return -1

    return res


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
