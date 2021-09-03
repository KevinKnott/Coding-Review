# Subdomain Visit Count: https://leetcode.com/problems/subdomain-visit-count/

# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

from types import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ourCount = defaultdict(int)

        for domain in cpdomains:
            count, fullDomain = domain.split(" ")
            count = int(count)

            subDomain = fullDomain.split('.')
            for i in range(len(subDomain)):
                split = '.'.join(subDomain[i:])
                ourCount[split] += count

        result = []

        for k, v in ourCount.items():
            temp = ' '.join([str(v), k])
            result .append(temp)

        return result


# Oh yeah this works like a charm
# Honestly it simply just parsing a string and adding it to ta count which is super easy
# This runs in O(N) time and space although splicing the strings for the key is quite
# a heavy operation

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
