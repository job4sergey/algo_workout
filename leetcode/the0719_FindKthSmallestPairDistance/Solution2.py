class Solution(object):
    def smallestDistancePair(self, ns, k):
        ns.sort()
        sz = len(ns)

        def bs(i, d):
            i0, j = i, sz

            while i < j - 1:
                m = i + (j - i) // 2
                if ns[m] - ns[i0] < d:
                    i = m
                else:
                    j = m

            return j

        def lt(d):
            i, cn = 0, 0

            while i < sz - 1:
                j = bs(i, d)
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
