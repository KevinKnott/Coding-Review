# Verifying an Alien Dictionary: https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

from types import List

# This problem comes down to creating a new sorted alphabet and creating your own str cmp. So if we use a array of size 26 we can put down the ordered value as a key pair with o(1)
# look up then all we have to do is figure out for each two words if the follow the new order with some exceptions of length


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        values = [0] * 26

        for val, char in enumerate(order):
            values[ord(char) - ord('a')] = val

        for i in range(1, len(words)):
            A = words[i-1]
            B = words[i]

            for j in range(len(A)):
                if j >= len(B):
                    return False

                # If the char doesn't match we can automatically end parsing these two
                # as it will either be lexicographical or invalid
                if A[j] != B[j]:
                    letterA = ord(A[j]) - ord('a')
                    letterB = ord(B[j]) - ord('a')

                    if values[letterA] >= values[letterB]:
                        return False
                    break

        return True

# The above works really well you could techincally change the array for a dict which may increase the look up speed of the second part but it is
# still going to end up as O(N) time and O(1) space as the alphabet only consists of lowercase letters aka 26 chars.

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 8
# Was the solution optimal? Yee
# Were there any bugs? Nee
# 5 5 5 5 = 5
