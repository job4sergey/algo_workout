# skip '' -> (
# AND
# ) -> ''
# theirs idea
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cn = 0
        res = []

        for j, c in enumerate(s):
            if (c == '(' and cn > 0) or (c == ')' and cn > 1):
                res.append(c)

            cn += 1 if c == '(' else -1

        return ''.join(res)

    def removeOuterParentheses0(self, s: str) -> str:
        cn = 0
        res = []

        for j, c in enumerate(s):
            if c == '(':
                if cn > 0:
                    res.append(c)
            else:
                if cn > 1:
                    res.append(c)

            cn += 1 if c == '(' else -1

        return ''.join(res)
