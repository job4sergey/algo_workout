from collections import defaultdict


class Solution(object):
    def regionsBySlashes(self, grid):
        g = defaultdict(list)

        def edge(r, c, se1, r2, c2, se2):
            g[(r, c, se1)].append((r2, c2, se2))
            g[(r2, c2, se2)].append((r, c, se1))

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell in '\\ ':
                    edge(r, c, 0, r, c, 3)
                    edge(r, c, 1, r, c, 2)
                if cell in '/ ':
                    edge(r, c, 0, r, c, 1)
                    edge(r, c, 3, r, c, 2)

                if c > 0:
                    edge(r, c, 0, r, c - 1, 2)

                if r > 0:
                    edge(r, c, 1, r - 1, c, 3)

        q = []
        vis = set()

        cn = 0

        for r0 in g:
            if r0 in vis:
                continue

            cn += 1

            q.append(r0)
            vis.add(r0)
            while q:
                r = q.pop()
                for r2 in g.get(r, []):
                    if r2 in vis:
                        continue

                    vis.add(r2)
                    q.append(r2)

        return cn
