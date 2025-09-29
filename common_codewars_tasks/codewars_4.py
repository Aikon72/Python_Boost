# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python
# Write a function that merges two sorted arrays into a single one. The arrays only contain integers.
# Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays(first, second):
   pass


def merge_arrays_olga(first, second):
    answer = sorted(list(set(first + second)))
    return answer


arr1 = [2, 4, 8]
arr2 = [2, 4, 6]

print(merge_arrays(arr1, arr2))
print(merge_arrays_olga(arr1, arr2))


def merge_list_denis (a, b):
    unique = []
    for item in a + b:
        if item not in unique:
            unique.append(item)
    unique.sort()
    return unique

print(merge_list_denis(arr1, arr2))