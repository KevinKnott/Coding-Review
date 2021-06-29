# Group Anagrams: https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# So the first solution that I can think of is actually taking a dictionary/counter and getting all the values and somehow creating that as a hash
# So that we can bucket the solutions together and return it

class Solution:
    def groupAnagrams(self, strs):
        result = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            # This won't work as we can't has by a dictionary
            # However if we convert this dict to a bitmap we may be able to solve the same way
            count = tuple(count)
            if count not in result:
                result[count] = []
            result[count].append(word)

        return [value for value in result.values()]

# This works and runs in o(n x m) time where n is the number of strings and m is the length of strings and it also takes up the same amount of space
# So is this the most optimal? I don't think so because technically we have to parse through everything a couple of times
# Instead we could sort every word which would be in n * mlog m time and then group by sorted which may be more efficient especially since we don't
# have to use even more auxilary space as this would sort words in place but overall is o(N * m) because we are bucketing the results

    def groupAnagrams(self, strs):
        result = {}

        for word in strs:
            # This word needs to be converted back into a str from a list
            temp = ''.join(sorted(word))
            if temp not in result:
                result[temp] = []
            result[temp].append(word)

        return [value for value in result.values()]


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Oh yea
# Were there any bugs? The bug I mentioned above
# 5 5 5 4 = 4.75
