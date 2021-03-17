class Solution:
    def isValid(self, s):
        st = []

        for c in s:
            if c == 'a':
                st.append(0)
            else:
                ordc = ord(c) - ord('a')
                if st and ordc - 1 == st[-1]:
                    st.pop()
                    if ordc < 2:
                        st.append(ordc)
                else:
                    return False

        return not st
