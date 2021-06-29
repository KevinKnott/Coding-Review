# Integer to English Words: https://leetcode.com/problems/integer-to-english-words/

# Convert a non-negative integer num to its English words representation.

# My initial thought here is to use a bunch of recursion to solve down the problem
# My reason for that is a lot of these problems have overlapping print statements
# that are based off of the number and then another number

class Solution:
    def numberToWords(self, num: int) -> str:
        def ones(num):
            switch = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'

            }
            return switch.get(num)

        def teens(num):
            switch = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switch.get(num)

        def ten(num):
            switch = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switch.get(num)

        # Case where we have the number 21 18 10
        def getTwo(num):
            if not num:
                return ''
            elif num < 10:
                return ones(num)
            elif num < 20:
                return teens(num)
            else:
                ourTen = num // 10
                rest = num - ourTen * 10
                return ten(ourTen) + ' ' + ones(rest) if rest else ten(ourTen)
            return

        # Case where we have numbers like 021 201 or 001
        def getThree(num):
            hundred = num // 100
            rest = num - hundred * 100

            if hundred and rest:
                return ones(hundred) + ' Hundred ' + getTwo(rest)
            elif not hundred and rest:
                return getTwo(rest)
            elif hundred and not rest:
                return ones(hundred) + ' Hundred'

        result = ""

        if not num:
            return 'Zero'

        # First split the numbers up into 4 segments billions/millions/thousands/hundreds
        billion, num = divmod(num, (10 ** 9))
        million, num = divmod(num, (10 ** 6))
        thousand, num = divmod(num, (10 ** 3))
        hundreds, num = divmod(num, 1)
        # Then append the numbers that you need from functions built for adding words

        if billion:
            result = getThree(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += getThree(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += getThree(thousand) + ' Thousand'
        if hundreds:
            result += ' ' if result else ''
            result += getThree(hundreds)

        return result

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? n
# Was the solution optimal? Maybe I am not sure
# Were there any bugs? Figuring out the actuall rules between spaces really messed me up quite a bit here
# 4 3 3 3 = 3.25
