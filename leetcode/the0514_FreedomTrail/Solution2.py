from collections import defaultdict


# level order traversal
class Solution(object):
    def findRotateSteps(self, ring, key):
        poss = defaultdict(list)  # character to positions mapping

        for i0, c in enumerate(ring):
            poss[c].append(i0)

        rsz = len(ring)
        ksz = len(key)

        def weight(i, j):  # min number of rotations of ring from i to j
            i1, j1 = min(i, j), max(i, j)
            return min(rsz - j1 + i1, j1 - i1)

        def main():
            res = float('inf')
            lev = [(0, 0)]  # weight, pos in ring
            lev2 = []
            j = 0  # current position in key
            dp = {}
            while lev:
                dp.clear()
                while lev:
                    w, i = lev.pop()
                    for p_j in poss[key[j]]:  # iterate all positions that can satisfy key[j]
                        # weight before + weight(rotate from i to p_j) + press button
                        w2 = w + weight(i, p_j) + 1
                        if j + 1 == ksz:  # key is matched
                            res = min(res, w2)
                            continue

                        w0 = dp.get(p_j, float('inf'))
                        if w0 <= w2:
                            continue
                        dp[p_j] = w2
                        lev2.append((w2, p_j))

                lev, lev2 = lev2, lev  # lev is empty, so no need to lev2.clear()
                j += 1

            return res

        return main()
