from collections import Counter


# """
# Idea :
# maintain stack of letters. while cur letter is less then one on the stack,
# if letter on the stack is not the last one. After that, push curr letter on the stack.
# Also maintain uniq array of letters already placed.
#
# In the end, stack will contain lexicographically smallest subsequence.
#
# """


class Solution(object):
    # mine
    def removeDuplicateLetters(self, s):
        fq = Counter(s)

        st = []
        uniq = set()

        for c in s:
            fq[c] -= 1
            if c in uniq:
                continue

            while st and st[-1] > c and fq[st[-1]] > 0:
                uniq.remove(st[-1])
                st.pop()

            uniq.add(c)
            st.append(c)

        return ''.join(st)

    # nice usage of last_occurrence
    def removeDuplicateLetters_theirs(self, s) -> int:

        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
