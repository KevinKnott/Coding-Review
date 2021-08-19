# Subdomain Visit Count: https://leetcode.com/problems/subdomain-visit-count/

# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
#     For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

# So this is a basic parsing problem in which you parse the input and store in a hash map and then return that hashmap as a list

from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        ourMap = defaultdict(int)

        for domain in cpdomains:
            count, fullDomain = domain.split(' ')
            count = int(count)

            subDomain = fullDomain.split('.')
            for i in range(len(subDomain)):
                split = '.'.join(subDomain[i:])
                ourMap[split] += count

        result = []

        for key, val in ourMap.items():
            temp = ' '.join([str(val), key])
            result.append(temp)

        return result

# The above works by basically spliting up the values to parse them correctly
# and then adding each possible subdomain into the hash map to add our count
# then we simply go through our map and add them to our result

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 7
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
