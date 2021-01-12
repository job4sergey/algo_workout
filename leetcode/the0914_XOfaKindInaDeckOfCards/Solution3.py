from collections import Counter


class Solution(object):
    def hasGroupsSizeX(self, cs):
        fq = Counter(cs)

        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        g = 0
        for cn in fq.values():
            g = gcd(g, cn)
            if g == 1:
                break

        return g > 1
