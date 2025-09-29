"""
https://www.codewars.com/kata/554b4ac871d6813a03000035

In this little assignment you are given a string of space separated
numbers, and have to return the highest and lowest number.

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

"""



# high_and_low = "1 2 3 4 5" # return "5 1"
# high_and_low = "1 2 -3 4 5" # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
numbers = "-905 -13 -808 -720 703 -274 503 -159 -113 615 992 -398 -47 191 808"

numbers = numbers.split()
d = []
for i in numbers:
    d.append(int(i))
b = max(d)
c = min(d)
numbers = str(b) + " " + str(c)

print(numbers)

#dmitry
a = "1 2 3 4 5 462 7653 417653"
a = a.split()
numbers = []
for i in a:
    numbers.append(i)
e = max(numbers)
f = min(numbers)

print(str(e) + " " + str(f))




























