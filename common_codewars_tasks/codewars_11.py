# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
#
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string

def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[1] == arr[2]:
            return arr[0]
        else:
            return arr[1]
    for i in range(2, len(arr)):
        if arr[i-1] != arr[i]:
            return arr[i]


arr = [1, 1, 1, 2, 1, 1, 1, 1]
print(find_uniq(arr))

#Dmitry
def find_uniq(arr):
    a = []
    b = []

    a.append(arr[0])
    if arr[0] == arr[1]:
        a.append(arr[1])
    else:
        b.append(arr[1])
    for c in arr[2:]:
        if c in a:
            a.append(c)
        if c not in a:
            b.append(c)
    if len(a) > len(b):
        return b[0]
    else:
        return a[0]

arr = [ 0, 0, 0.55, 0, 0 ]
print(find_uniq(arr))


# Вариант решения от Маша

# array = [ 0, 3, 0, 0, 0, 0 ]
#
# def find_uniq(arr):
#     for i in range(0, len(arr) - 1):
#         if arr[i] != arr[i+1]:
#             if i == 0 and arr[1] == arr[2]:
#                 return arr[0]
#             else:
#                 return arr[i+1]
#
# print(find_uniq(array))