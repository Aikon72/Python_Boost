# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python
# Write a function that merges two sorted arrays into a single one. The arrays only contain integers.
# Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays_olga(first, second):
    answer = sorted(list(set(first + second)))
    return answer


def merge_list_denis (a, b):
    unique = []
    for item in a + b:
        if item not in unique:
            unique.append(item)
    unique.sort()
    return unique


#Dmitry
def merge_arrays(first, second):
    a = first + second
    a = sorted(a)
    result = []
    for i in a:
        if i not in result:
            result.append(i)
        elif i in result:
            del(i)
    return result


def merge_arrays_serge(first, second):
    res = []
    first_index = 0
    second_index = 0
    while first_index < len(first) or second_index < len(second):
        if first_index >= len(first):
            if not res or second[second_index] != res[-1]:
                res.append(second[second_index])
                second_index += 1
        elif second_index >= len(second):
            if not res or first[first_index] != res[-1]:
                res.append(first[first_index])
                first_index += 1
        elif first[first_index] == second[second_index]:
            if not res or first[first_index] != res[-1]:
                res.append(first[first_index])
                first_index += 1
                second_index += 1
        elif first[first_index] < second[second_index]:
            if not res or first[first_index] != res[-1]:
                res.append(first[first_index])
                first_index += 1
        else:
            if not res or second[second_index] != res[-1]:
                res.append(second[second_index])
                second_index += 1
    return res


arr1 = [2, 4, 8]
arr2 = [2, 4, 6]


print(merge_arrays_olga(arr1, arr2))
print(merge_list_denis(arr1, arr2))
print(merge_arrays(arr1, arr2))
print(merge_arrays_serge(arr1, arr2))