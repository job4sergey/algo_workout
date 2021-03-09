class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s, sz):
            for k in range(len(s) - sz + 1):
                i, j = k, k + sz - 1

                while i < j:
                    if s[i] != s[j]:
                        break

                    i += 1
                    j -= 1

                if i >= j:
                    return s[k:k + sz]

            return ''

        def bs(cn, is_odd):
            i = 0
            j = cn + 1
            mx = ''
            while i < j - 1:
                m = i + (j - i) // 2
                sz = m * 2 - is_odd
                res = check(s, sz)
                if res:
                    mx = res
                    i = m
                else:
                    j = m

            return mx

        def main():
            sz = len(s)
            mx1, mx2 = bs(sz // 2, 0), bs(sz - sz // 2, 1)
            return max((mx1, mx2), key=len)

        return main()
