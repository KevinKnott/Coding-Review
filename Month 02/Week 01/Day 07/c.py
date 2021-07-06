# Verifying an Alien Dictionary: https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# Okay so this is a simple sorting algorithm where you compare two words moving through all of them and if any are out of order you simply return false
# Otherwise the solution is true

# We can use a dictionary to conver the letter to a numerical value a being 0 z being 26 (except with random letters) and then we can compare the
# sort using this dict

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        alienValue = {}

        for index, value in enumerate(order):
            alienValue[value] = index

        # Now that we have numerical values we need to compare words as we go
        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]

            # now loop through each if word1 is the same but longer than word2 we need to return false
            for j in range(len(word1)):
                # If word 2 is the same as word 1 but is shorter then we know the ordering is wrong
                if j >= len(word2):
                    return False

                # Only need to return false if there is a mismatch
                if word1[j] != word2[j]:
                    if alienValue[word1[j]] > alienValue[word2[j]]:
                        return False

                    break

        return True

# The above works and is pretty intuitive it runs in worst case o(m) where m is all letters of all of the words
# this is techincally in o(1) space as the valuing of the alien language uses only 26 characters which is a constant


# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? 20
# Was the solution optimal? See above
# Were there any bugs? Nope
# 2 5 5 5 = 4.25
