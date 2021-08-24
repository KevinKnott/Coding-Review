# Minimum Remove to Make Valid Parentheses: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# This problem seems really tricky but honestly you are checking that whenever you add a ( or ) that it is valid
# otherwise you add it to your count
# so the two ones are if you have a ( it is only valid if you have a ) so if you find a ) after it at somepoint it is valid
# or if you have a ) there has to be something before it aka ( so if you have an empty stack you can add it to the count
# Now the other piece of this is you need to add all ( and remove them once you have a valid combo as it has been
# validated

# Oh I read this a bit wrong since we need to return a valid string our stack needs to hold the index at which the invalid parens
# are so that we can remove them before returning

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for index in range(len(s)):
            char = s[index]

            if char == ')':
                if len(stack) == 0:
                    stack.append(index)
                else:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(index)

            elif char == '(':
                stack.append(index)

        result = ''
        index = 0
        for i in range(len(s)):
            if index < len(stack) and stack[index] == i:
                index += 1
                continue

            result += s[i]

        return result

# The above works but there is definitely some improvements that could be made as I am not using a set to remove values
# but rather going across iteratively. The reason why we could use a set is that we know if a value is invalid by if it
# is still on the stack once we have finished parsing or if we have an invalid char befor it.

# The above runs in O(N) and uses O(N) space and actually so will this second piece but it will be a slight improvement
# as the string building will be using an O(1) that requires no extra operations

    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    remove.add(i)

        while stack:
            remove.add(stack.pop())

        result = ''
        for i in range(len(s)):
            if i not in remove:
                result += s[i]

        return result

# This is just a slight improvement and doesn't effect the big O

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
