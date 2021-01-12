class Solution(object):
    def smallestDistancePair(self, ns, k):
        ns.sort()
        sz = len(ns)

        def lt(d):
            i, j, cn = 0, 1, 0

            while i < sz - 1:
                while j < sz and ns[j] - ns[i] < d:
                    j += 1

                cn += j - i - 1
                i += 1

            return cn

        def doit():
            i, j = ns[1] - ns[0] - 1, ns[sz - 1] - ns[0] + 1

            while i < j - 1:
                m = i + (j - i) // 2
                if lt(m) < k:
                    i = m
                else:
                    j = m

            return i

        return doit()
