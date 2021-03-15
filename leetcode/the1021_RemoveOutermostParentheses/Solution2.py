# idea - if we have reached empty stack ->
# then we have finished examination of primitive subsequence
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        res = []

        for j, c in enumerate(s):
            if c == '(':
                st.append(j)
            else:
                i = st.pop()
                if not st:
                    res.append(s[i + 1:j])

        return ''.join(res)
