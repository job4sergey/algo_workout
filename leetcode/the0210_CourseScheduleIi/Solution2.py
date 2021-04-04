from collections import defaultdict


class Solution(object):
    def findOrder(self, N, es):
        ind = [0] * N
        res = []

        g = defaultdict(list)

        for v, u in es:
            ind[v] += 1
            g[u].append(v)

        q = [u for u, deg in enumerate(ind) if deg == 0]
        while q:
            u = q.pop()
            res.append(u)
            for v in g.get(u, tuple()):
                ind[v] -= 1
                if not ind[v]:
                    q.append(v)

        if len(res) != N:
            res.clear()

        return res
