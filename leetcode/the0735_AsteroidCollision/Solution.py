class Solution:
    def asteroidCollision(self, asrs):
        st = []

        for a in asrs:
            while st and st[-1] > 0 > a:
                b = st[-1]
                if abs(b) < abs(a):
                    st.pop()
                elif abs(b) == abs(a):
                    a = 0
                    st.pop()
                    break
                else:
                    a = 0
                    break

            if a:
                st.append(a)

        return st
