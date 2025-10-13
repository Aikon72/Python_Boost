
'''https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''


# Решение от Юлии:

def count_vowels(n):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in n:
        if i in vowels:
            count += 1
    return count

print(count_vowels('Hello'))
print(count_vowels('Yuliya'))