# Reorder Data in Log Files: https://leetcode.com/problems/reorder-data-in-log-files/

# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

#     Letter-logs: All words (except the identifier) consist of lowercase English letters.
#     Digit-logs: All words (except the identifier) consist of digits.

# Reorder these logs so that:

#     The letter-logs come before all digit-logs.
#     The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
#     The digit-logs maintain their relative ordering.

# Return the final order of the logs.

class Solution:
    def reorderLogFiles(self, logs):
        return

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
