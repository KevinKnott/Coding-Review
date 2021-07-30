# Verifying an Alien Dictionary: https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# This problem is just creating a custom comparitor where we change the numerical value of the alphabet
# todo this we can simply use a hashmap and create a comparitor then compare each word to its adjacent partner
# if we fail return false other wise return true

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        if len(words) == 1:
            return True

        value = {}
        for index, letter in enumerate(order):
            value[letter] = index

        for i in range(1, len(words)):
            # compare each word ch by ch
            for j in range(len(words[i-1])):
                # In the case the second word is shorter than the first but match otherwise
                # we return false
                if j >= len(words[i]):
                    return False

                # if they match w/e we keep going
                if words[i-1][j] != words[i][j]:
                    # otherwise we need to check if i-1 < i
                    if value[words[i-1][j]] > value[words[i][j]]:
                        return False
                    # We can always tell if lexigraphic order after one different letter
                    # So we break if we don't return False
                    break
        return True


# This is the optimal solution it runs in o(M) time as we have m characters in N words
# and uses o(1) space as we only store the key/value of 26 chars

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 12
# Was the solution optimal? See above
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
