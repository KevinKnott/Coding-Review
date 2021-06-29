# Integer to English Words: https://leetcode.com/problems/integer-to-english-words/
# Convert a non-negative integer num to its English words representation.

# After writting down a few examples I think the best way to do this is by sections of 3
# every time we go up by 3 we actually add a height word to the end ie (null, hundred, thousand, million, billion)
# then we have the following per 3
#  Number  hundred  Number+tensplace (seventy/sixty) number (height)

# I forgot eleven tweleve ...

# Create an enum/dict then follow the above pattern?


class Solution:
    # Initial thought but this is rough
    # def __init__(self):
    #     self.height = {0: None, 1: 'Hundred', 2: 'Thousand', 3: 'Million', 4: 'Billion'}
    #     self.tens = {''}
    #     self.ten = {''}
    #     self.ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',}

    def numberToWords(self, num: int) -> str:
        # Convert all the types of numbers
        def one(num):
            switcher = {
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
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
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
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            # Given some numbers like
            # 00 -> ''
            # 9 -> Nine (pass to one)
            # 19 -> Nineteen (pass to two less than 20)
            # 29 -> Figure out special ten values
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                # Grab tens place to make Twenty, Thirty etc
                tenner = num // 10
                # Pass the rest to one as we have Twenety Five
                # or rest is nothing and we just pass back then tens place
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            # If there are 3 values then we need to add a 'Hundred'
            hundred = num // 100
            # Then get the rest and pass it down
            rest = num - hundred * 100
            # 233 -> Two Hundred and rest
            # 023 -> rest (twenty three) (height)
            # 200 -> Two Hundred (height)
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        # Take our number and reduce each piece
        # From top down since we don't care about negative numbers as we go down we just remove that much
        # Alternatively we could go by length and reduce it but that is more comlex
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        # If we remove all the
        if not num:
            return 'Zero'

        # Build the result up
        result = ''
        if billion:
            # If there is a billions place call out to however many billions we have
            result = three(billion) + ' Billion'
        if million:
            # Then add the millions (Add space if we have previous)
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            # Then add the thousand (Add space if we have previous)
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            # Then add the rest (Add space if we have previous)
            result += ' ' if result else ''
            result += three(rest)
        return result

# Score Card
# Did I need hints? Ish
# Did you finish within 30 min? N
# Was the solution optimal? The result ends up parsing in O(N) but it is divide and conquer
# Were there any bugs? So many edge cases for english
#  2 1 4 2 = 2.25
