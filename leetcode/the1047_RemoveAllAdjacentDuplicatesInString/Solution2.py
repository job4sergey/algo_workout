class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = ['Z']

        for c in s:
            if st[-1] == c:
                st.pop()
            else:
                st.append(c)

        return ''.join(st[1:])
