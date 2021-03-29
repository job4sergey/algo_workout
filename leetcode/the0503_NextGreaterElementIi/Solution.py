class Solution(object):
    def nextGreaterElements(self, ns):
        def bsr(a, x):
            i, j = -1, len(a)

            while i < j - 1:
                m = i + (j - i) // 2
                if a[m] <= x:
                    j = m
                else:  # a[m] > x
                    i = m

            return i

        def main():
            res = [-1] * len(ns)

            st = []
            rescan = []
            for i in range(len(ns) - 1, -1, -1):
                while st and st[-1] <= ns[i]:
                    st.pop()

                if st:
                    res[i] = st[-1]
                else:
                    rescan.append(i)
                st.append(ns[i])

            for i in rescan:
                j = bsr(st, ns[i])
                res[i] = st[j] if j > -1 else -1

            return res

        return main()
