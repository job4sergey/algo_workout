class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []

        for c in s:
            if c == '(':
                st.append('(')
            else:
                sm = 0
                while st[-1] != '(':
                    sm += st.pop()

                st.pop()

                sm *= 2
                if sm == 0:
                    sm = 1

                st.append(sm)

        return sum(st)
