# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example: ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    pass

def remove_every_other_Olga(my_list):
    i = 1
    n = len(my_list)
    while i < n:
        my_list.pop(i)
        i += 1
        n -= 1
    return my_list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(remove_every_other(arr))