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

# So we are given an array of logs and we are to sort them by letter log, then digit log. Also the letter log is to be lexicographically sorted
# Which basically means that this comes down to a simple parsing problem then sorting the letters and recombining the lists

class Solution:
    def reorderLogFiles(self, logs):
        letterLog = []
        digitLog = []

        # Since we have to go log by log we could inject the log in o(n) with an insertion sort
        # but for simplicity I will just use the built in sort which is nlogn

        for log in logs:
            identifier, values = log.split(' ', 1)

            # Now we need to check for if we have digit or letter
            if values[0].isalpha():
                letterLog.append([identifier, values])
                letterLog.sort(key=lambda x: x[0])
                letterLog.sort(key=lambda x: x[1])
            else:
                digitLog.append(log)

        result = []

        for i in range(len(letterLog)):
            result.append(' '.join(letterLog[i]))

        return result + digitLog


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Yup this is optimal and runs in O(M * N log N) as we go through all digit/letter logs and sort the letterlogs
# Were there any bugs? None
# 5 5 5 5 = 5
