# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example: ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other_sb(my_list):
    arr = []
    k = True
    for c in my_list:
        if k:
            arr.append(c)
        k = not k
    return arr

def remove_every_other_serge(my_list):
    return my_list[::2]

def remove_every_other_Olga(my_list):
    i = 1
    n = len(my_list)
    while i < n:
        my_list.pop(i)
        i += 1
        n -= 1
    return my_list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_every_other_sb(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_every_other_serge(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_every_other_Olga(arr))