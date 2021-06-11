# Decode String: https://leetcode.com/problems/decode-string/
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

#  this problem reminds me of the Element problem from the other day
#  Loop through the array if there is a digit we know that we need to add a string repetitievly

# Ran out of time I just need to implement the recursive piece to work for this 1[ab2[c]]e
# As my code initially woulld break because I wasn't initially recursion on []
class Solution:
    def decodeString(self, s: str) -> str:
        self.index = 0
        result = ''

        def parse():
            result = ''
            while self.index < len(s) and s[self.index] != ']':
                if s[self.index].isdigit():

                    start = self.index
                    # Step over current number
                    self.index += 1
                    while self.index < len(s) and s[self.index] != '[':
                        self.index += 1
                    repeat = int(s[start: self.index])
                    # Step over '['
                    self.index += 1

                    temp = parse()
                    # start = self.index
                    # while self.index < len(s) and s[self.index] != ']':
                    #     self.index += 1
                    result += repeat * temp

                else:
                    result += s[self.index]
                    self.index += 1

            self.index += 1
            return result

        result = parse()
        return result

# It took me about an hour and 10 to do this but I figured it out
#  this solution is a o(N)  time and o(k) space where k is the number of [] (we recurse each time we see one)

# There is a slightly easier solution that I didn't see though
    def decodeStringStacks(self, s: str) -> str:
        curString = ''
        count = []
        strings = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                count.append(int(s[start:i]))
                strings.append(curString)
                curString = ''

            elif s[i] == ']':
                curString = strings.pop() + count.pop() * curString

            else:
                curString += s[i]

            i += 1
        return curString


# Score Card
# Did I need hints? N (But the second solution did)
# Did you finish within 30 min? No 1:30
# Was the solution optimal? My initial solution is optimal however I messed up the initial coding of it
# Were there any bugs? I forgot that since it is possible to have [[[[]]]] I need to actually recurse
#  4 1 2 1 = 2
