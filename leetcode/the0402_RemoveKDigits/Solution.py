class Solution:
    def removeKdigits(self, ns: str, k: int) -> str:
        if k == len(ns):
            return '0'

        st = []

        for n in ns:
            while st and st[-1] > n and k:
                st.pop()
                k -= 1

            if st or n != '0':
                st.append(n)

        while k:
            st.pop()
            k -= 1

        if not st:
            st.append('0')

        return ''.join(st)
