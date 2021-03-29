class Solution(object):
    def uniquePathsIII(self, g):
        rc, cc = len(g), len(g[0])

        def inits():
            fro = (0, 0)
            cn = 0
            for x in range(rc):
                for y in range(cc):
                    if g[x][y] == 1:
                        fro = (x, y)
                        cn += 1
                    elif g[x][y] in (0, 2):
                        cn += 1

            return fro, cn

        fro, num_free = inits()

        def rec(x, y, cn=1):
            res = 0

            if g[x][y] == 2:
                return 1 if cn == num_free else 0

            g[x][y] = -1

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 <= rc - 1 and 0 <= y2 <= cc - 1 and g[x2][y2] in (0, 2):
                    res += rec(x2, y2, cn + 1)

            g[x][y] = 0

            return res

        return rec(fro[0], fro[1])
