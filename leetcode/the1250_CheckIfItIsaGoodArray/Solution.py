# Bezout identity
class Solution(object):
    def isGoodArray(self, ns):
        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        def gcdx(ar):
            g = 0

            for x in ar:
                g = gcd(g, x)
                if g == 1:
                    break

            return g

        return gcdx(ns) == 1
