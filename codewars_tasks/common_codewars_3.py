"""https://www.codewars.com/kata/541c8630095125aba6000c00
Description:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
 16  -->  1 + 6 = 7
 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digital_root(n):
    while n >= 10:
    new = []
        if len(str(n)) == 1:
            print (n)
        if len(str(n)) > 1:
            for c in str(n):
                new.append(int(c))
                print(sum(new))
    pass # your code here

print(digital_root(578878786))