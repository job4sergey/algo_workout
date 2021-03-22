class Solution(object):
    def mostCompetitive(self, ns, k):
        st = []

        for i, n in enumerate(ns):
            left = len(ns) - i - 1
            while st and st[-1] > n and k - len(st) <= left:
                st.pop()

            if len(st) < k:
                st.append(n)

        return st
