# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example: ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!
import time
import random

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

    return [my_list[i] for i in range(0, len(my_list), 2)]


arr = [random.randint(1,100) for _ in range(1000) ]


method = "sb"
print("Проверяю метод: ", method)
t1 = time.perf_counter()
print(remove_every_other_sb(arr))
t2 = time.perf_counter()
print(t2-t1)
max_value = t2 - t1
quick_method = method

method = "deepseek"
print("Проверяю метод: ", method)
t1 = time.perf_counter()
print(remove_every_other_serge(arr))
t2 = time.perf_counter()
print(t2-t1)
if t2 - t1 > max_value:
    max_value = t2 - t1
    quick_method = method

method = "Olga"
print("Проверяю метод: ", method)
t1 = time.perf_counter()
print(remove_every_other_Olga(arr))
t2 = time.perf_counter()
print(t2-t1)
if t2 - t1 > max_value:
    max_value = t2 - t1
    quick_method = method

print("Самый быстрый метод у: ", quick_method)

