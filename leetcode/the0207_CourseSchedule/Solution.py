from collections import defaultdict


class Solution(object):
    def canFinish(self, no, deps):
        g = defaultdict(list)

        for d in deps:
            g[d[0]].append(d[1])

        color = [2] * no

        def dfs(r):
            if color[r] == 0:
                return True

            if color[r] == 1:
                return False

            color[r] = 1

            for r2 in g.get(r, []):
                if not dfs(r2):
                    return False

            color[r] = 0

            return True

        for r0 in g:
            if not dfs(r0):
                return False

        return True
