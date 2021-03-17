# theirs
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]

        for c in s:
            if c == '(':
                st.append(0)
            else:
                x = st.pop()
                st[-1] += max(x * 2, 1)

        return st[0]
