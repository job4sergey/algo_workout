class Solution(object):
    def flipMatchVoyage(self, r0, vals):
        st = []
        if r0.val != vals[0]:
            return [-1]
        i = 1

        if r0.right:
            st.append((0, r0))

        if r0.left:
            st.append((1, r0))

        res = []

        while st:
            is_left, p = st.pop()
            r = p.left if is_left else p.right

            if r.val != vals[i]:
                res.append(p.val)
                p.left, p.right = p.right, p.left
                r = p.left if is_left else p.right
                if not r or r.val != vals[i]:
                    return [-1]

            i += 1

            if r.right:
                st.append((0, r))

            if r.left:
                st.append((1, r))

        return res
