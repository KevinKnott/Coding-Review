# Group Anagrams: https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# So the first solution that comes to mind is create a dicitonary of letters and counts of each letter and hashing them together
# the problem with this is that dicts arent a hashable type so we must convert them to a tuple which is a o(n) step. Also tuples
# can be used as the are immutable. Also instead of using dicts we should use a list of len 26 as it will take O(1) space and
# allow us to not need to sort the letters in a dictionary

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for word in strs:
            hash = [0] * 26

            for ltr in word:
                hash[ord(ltr) - ord('a')] += 1

            result[tuple(hash)].append(word)

        return [v for v in result.values()]

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8 min
# Was the solution optimal? This is optimal but runs in O(NK) for time and space where N is the num of words
# and k is the len of longest word
# Were there any bugs? Negative
# 5 5 5 5 = 5
