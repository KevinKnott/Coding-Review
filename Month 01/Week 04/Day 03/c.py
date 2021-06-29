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

# My first thought with this problem is creating an array to hold these values and then do an insertion sort to add things with a custom comparator

class Solution:
    def reorderLogFiles(self, logs):
        letterLog = []
        digitLog = []

        for log in logs:
            first = log.split(" ", 2)[1]

            # Loop through the values and determine which comes first
            if first.isdigit():
                digitLog.append(log)
            else:
                letterLog.append(log)

        letterLog.sort(key=lambda x: x.split(' ')[0])
        letterLog.sort(key=lambda x: x.split(' ', 1)[1:])

        return letterLog + digitLog

# The above took me a bit of time as there were a few cases I didn't think of mainly revolving around the fact that the digit logs are already sorted
# So basically you just append them at the end. Other than that I wrote a custom comparator but honestly it was a bit convoluted so I resorted to
# just using a builtin one but splitting the values based off of the identifier and then the rest

# Score Card
# Did I need hints? Y I haven't looked at comparators in a minute so I looked one up to help me out
# Did you finish within 30 min? 30 Y
# Was the solution optimal? There may be a faster way than what I did but this runs in O(m * nlogn) where m is the lenght of a log and N is the number of logs
# as for space it runs in O(M*N) as we store every log
# Were there any bugs? None
# 3 5 4 5 = 4.25
