# Integer to English Words: https://leetcode.com/problems/integer-to-english-words/

# Convert a non-negative integer num to its English words representation.

# So this problem seems rather complicated but honestly it is simpler than you think
# all we have to do is break down each piece from ones -> thousands -> millions -> billions
# and then we can simply do the same thing for each 3 numbers because 23 at then end looks the same
# in any of those spots

# The tricky piece is that 0 - 19 all have stupid silly differences so they will have to be broken down
# properly

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        def convertThree(num):
            # So all we need to do is create all the possible splits
            # 135 100 101 110 113 005 015
            # One hundred call converTwo on thirty five
            # One hundred call converTwo on
            # One hunderd call converTwo on One
            # One hundred call converTwo on ten
            # One hundred call converTwo on thirteen
            # call converTwo five
            # call converTwo fifteen

            # Split the number at 1 35
            hundred, rest = divmod(num, 100)

            # I took these from above
            if hundred and rest:
                return ones(hundred) + ' Hundred ' + convertTwo(rest)
            elif hundred and not rest:
                return ones(hundred) + ' Hundred'
            elif not hundred and rest:
                return convertTwo(rest)

            return ' '

        def convertTwo(num):
            # So now we need to split up the two digit results
            # 0 10 15 19 20 31 48
            # Zero this needs to be added to the first
            # Ten call twoBelow20
            # 15 call twoBelow20
            # 20 call tens
            # Thirty one split call tens and then ones
            # the rest fall into the category of above

            if not num:
                return ''
            elif num < 10:
                return ones(num)
            elif num < 20:
                return twoBelow20(num)
            else:
                # We need to split number and call ones and tens
                tensPlace, rest = divmod(num, 10)
                return tens(tensPlace) + ' ' + ones(rest) if rest else tens(tensPlace)

        def ones(num):
            switch = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine"
            }
            return switch[num]

        def twoBelow20(num):
            switch = {
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return switch[num]

        def tens(num):
            switch = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety"
            }
            return switch[num]

        # First we need to split up all of the numbers to each place using a divmod of 1000 for each 3 number split
        # 1234567891
        num, onesPlace = divmod(num, 1000)
        num, thousandsPlace = divmod(num, 1000)
        num, millionsPlace = divmod(num, 1000)
        num, billionsPlace = divmod(num, 1000)

        # Now that we have all of the separated numbers all we have to do is map them to (specific number) (place)
        result = ''
        if billionsPlace:
            result += convertThree(billionsPlace) + ' Billion'
        if millionsPlace:
            result += ' ' if result else ''
            result += convertThree(millionsPlace) + ' Million'
        if thousandsPlace:
            result += ' ' if result else ''
            result += convertThree(thousandsPlace) + ' Thousand'
        if onesPlace:
            result += ' ' if result else ''
            result += convertThree(onesPlace)

        return result

# So this problem is pretty simple it runs in o(n) time and o(1) space
# I will say this problem on leet code is stupid obnoxious as white space and spelling matter so much

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Yup
# Were there any bugs? I forgot the case where you need white space at the end of each place only if we are adding more onto the problem
# 5 5 5 3 = 4.5
