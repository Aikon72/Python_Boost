# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    counter_0 = 0
    # Какой цикл?
    # sb/Было бы неплохо While, но For должен сработать тоже
    # sb:Добавлять в конец - это я помню .append , а как вырезать?
    for i in range(0, len(lst)):




    return lst

arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(move_zeros(arr))