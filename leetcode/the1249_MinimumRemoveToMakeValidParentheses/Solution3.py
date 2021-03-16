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

        if not st:
            return s

        res = []
        j = 0
        for i, c in enumerate(s):
            if j == len(st):
                res.append(s[i:])
                break
            elif st[j] == i:
                j += 1
                continue

            res.append(c)

        return ''.join(res)
