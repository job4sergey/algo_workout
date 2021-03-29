class Solution(object):
    def isBipartite(self, g):
        sz = len(g)
        cls = [-1] * sz  # coloring

        def dfs(u0):
            if cls[u0] != -1:
                return True

            q = [u0]
            cls[u0] = 0
            while q:
                u = q.pop()
                c = cls[u]  # current color

                ecv = (c + 1) % 2  # expected color
                for v in g[u]:
                    if cls[v] == -1:
                        cls[v] = ecv
                        q.append(v)
                    elif cls[v] != ecv:
                        return False

            return True

        def main():
            for u in range(sz):
                if not dfs(u):
                    return False

            return True

        return main()
