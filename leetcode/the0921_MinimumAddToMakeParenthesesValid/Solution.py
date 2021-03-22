class Solution(object):
    def minAddToMakeValid(self, s):
        st = []

        for c in s:
            if c == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)

        return len(st)
