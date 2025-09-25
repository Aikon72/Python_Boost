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

def move_zeros_from_codewars(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array

arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(move_zeros_serge(arr))
print(move_zeros_from_codewars(arr))