#  Subdomain Visit Count: https://leetcode.com/problems/subdomain-visit-count/

# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# This kind of seems like a dfs problem where you split the string at each period and add a number to a count

from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        result = Counter()

        def dfs(count, current):
            if current == "":
                return

            result[current] += count

            index = 0
            while index < len(current) and current[index] != '.':
                index += 1

            dfs(count, current[index+1:])

        for i in cpdomains:
            count, word = i.split(' ')
            dfs(int(count), word)

        output = []
        for key, value in result.items():
            output.append(str(value) + ' ' + str(key))

        return output

# The above works and is capable of spliting up the problem
# However is this the best solution? I don't think so this splits the problem up and uses recursive stacking
# I think we can do the same thing except parse the string as we go
# this will optimize for space but is stil o(n^2) in the worst

    def subdomainVisitsOptimized(self, cpdomains):
        result = Counter()

        for i in cpdomains:
            count, word = i.split(' ')
            # Check if word is not empty
            while word != '':
                result[word] += int(count)

                # Other wise increase count move onto the next .
                index = 0
                while index < len(word) and word[index] != '.':
                    index += 1

                # continue indefinitely
                word = word[index+1:]

        # loop through counter for result
        output = []

        for key, value in result.items():
            output.append(str(value) + ' ' + str(key))

        return output

    # most optimized we can literally loop as we go through the fragments which would optimize almost the same
    def subdomainVisits(self, cpdomains):
        ans = Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? My initial solution is optimal
# Were there any bugs? None
# 4 5 3 5 = 4.25
