class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st and s[st[-1]] == '(':
                    st.pop()
                else:
                    st.append(i)

        sts = set(st)

        res = []
        for i, c in enumerate(s):
            if i not in sts:
                res.append(c)

        return ''.join(res)
