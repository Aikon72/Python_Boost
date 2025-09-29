# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros_serge(lst):
    counter_0 = 0
    i = 0
    while (i < len(lst)-counter_0):
        if lst[i] == 0:
            counter_0 += 1
            lst.pop(i)
            lst.append(0)
            i -= 1
        i += 1
    return lst

def move_zeros_olga(lst):
    counter_0 = i = 0
    n = len(lst)
    while i < n:
        if lst[i] == 0:
            del lst[i]
            counter_0 += 1
            n -= 1
        else:
            i += 1
    return lst + [0] * counter_0

def move_zeros_from_codewars(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array

arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(move_zeros_serge(arr))
print(move_zeros_olga(arr))
print(move_zeros_from_codewars(arr))

#Dmitry
def move_zeros(lst):
    for c in lst:
        if c == 0:
            lst.remove(c)
            lst.append(0)

    return lst