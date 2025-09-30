#  https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit, ]
# continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def summa (a):
    while a  >= 10:
        b = []
        for i in str(a):
            b.append(int(i))
            a = sum(b)
    return a

#Dmitry
def digital_root(n):
    while n >= 10:
        n = str(n)
        a = []
        for i in n:
            a.append(int(i))
            n = sum(a)

    return n

#тестовый комментарий
#тестовый комментарий2
#тестовый комментарий

def digital_root_serge(n):
# Я это уже решал в задаче 3
    return n

n = 493193

print(summa(n))
print(digital_root(n))
print(digital_root_serge(n))

# тестовый комент