class Solution:
    def backspaceCompare(self, s1: str, s2: str) -> bool:
        def apply(s):
            st = []

            for c in s:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)

            return st

        return apply(s1) == apply(s2)
