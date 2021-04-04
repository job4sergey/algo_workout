from collections import defaultdict


class Solution(object):
    def findOrder(self, N, es):
        g = defaultdict(list)
        for u, v in es:
            g[u].append(v)

        for u in range(N):
            if u not in g:
                g[u] = list()

        clr = [2] * N  # 2 - white, 1 - gray, 0 - black
        res = []

        def dfs(u):
            nonlocal res
            if clr[u] == 0:
                return True
            elif clr[u] == 1:
                return False

            clr[u] = 1
            for v in g[u]:
                if not dfs(v):
                    return False

            res.append(u)
            clr[u] = 0

            return True

        for u in g:
            if not dfs(u):
                return []

        return res
