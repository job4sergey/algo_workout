class Solution(object):
    def closedIsland(self, g):
        rc, cc = len(g), len(g[0])

        def wave(r0, c0):
            if g[r0][c0]:
                return 0

            g[r0][c0] = 2
            st = [(r0, c0)]
            while st:
                r, c = st.pop()

                for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    r2, c2 = r + dr, c + dc
                    if r2 < 0 or c2 < 0 or r2 == rc or c2 == cc or g[r2][c2]:
                        continue

                    g[r2][c2] = 2
                    st.append((r2, c2))

            return 1

        cn = 0

        for r in range(0, rc):
            wave(r, 0)
            wave(r, cc - 1)

        for c in range(0, cc):
            wave(0, c)
            wave(rc - 1, c)

        for r in range(1, rc - 1):
            for c in range(1, cc - 1):
                cn += wave(r, c)

        return cn
