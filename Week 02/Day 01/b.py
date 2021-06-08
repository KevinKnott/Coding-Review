#  Count Binary Substrings: https://leetcode.com/problems/count-binary-substrings/

# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# Brute force solution here TLE because it is o(n^2)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            start = s[i]
            swapped = False
            balance = 1
            j = i + 1

            while j < len(s) and balance >= 0:
                if balance == 0:
                    # print(s[i:j])
                    count += 1
                    break

                if s[j] != start:
                    balance -= 1
                    swapped = True
                else:
                    if swapped == True:
                        break
                    balance += 1

                j += 1

            if j == len(s) and balance == 0:
                count += 1

        return count

    # Apparently there is a better solution but I will have to look at hints
    def countBinarySubstringsOptimal(self, s: str) -> int:
        count = 0
        bucket = [1]
        # Create a bucket increasing the number of top everytime you see a similar char
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                bucket[-1] += 1
            # otherwise put a 1 on the top of the bucket
            else:
                bucket.append(1)

        # This will give us an array of number of 0s next to 1s and vice versa
        # Then we can loop through and take the minimum of the two as they are matched up to the smaller of the two
        # ie: [4, 2] could represent 000011 or 110000 either way you will match 0011 and 01 for your answer to increase by 2
        for i in range(1, len(bucket)):
            count += min(bucket[i], bucket[i-1])

        return count

    # There is even a way to do this in place if we simply convert the code above to check either the current flipped value or the last
    def countBinarySubstringsOnePass(self, s: str) -> int:
        count, prev, cur = 0, 0, 1
        # Create a bucket increasing the number of top everytime you see a similar char
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count += min(prev, cur)
                prev, cur = cur, 1
            # otherwise put a 1 on the top of the bucket
            else:
                cur += 1

        # Only difference is that we need to add the last piece on since this terminates before the last calc
        return count + min(prev, cur)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? Y  (no support for max heaps made me use negatives and I forgot to handle them properly)
#  2 1 3 4 = 2.5
