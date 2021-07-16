# Subdomain Visit Count: https://leetcode.com/problems/subdomain-visit-count/

# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# This problem is a simple hashing problem all we have to do is split the domains as we go across and add the value to a dictionary
# Then at the end we simply print out the key value par in a list

class Solution:
    def subdomainVisits(self, cpdomains):
        domainCount = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)

            subDomain = domain.split('.')
            for i in range(len(subDomain)):
                split = '.'.join(subDomain[i:])
                if split not in domainCount:
                    domainCount[split] = 0
                domainCount[split] += count

        result = []

        for key, value in domainCount.items():
            temp = ' '.join([str(value), key])
            result.append(temp)

        return result

# The above works and has no big issues!
# It runs in o(n) time and space but honestly creating each split of the domain
# could be reduced if I took more time with it


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 9
# Was the solution optimal? Yee
# Were there any bugs?  Nee
# 5 5 5 5 = 5
