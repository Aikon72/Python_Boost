# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    counter_0 = 0
    # Какой цикл?
    # sb/Было бы неплохо While, но For должен сработать тоже
    # sb:Добавлять в конец - это я помню .append , а как вырезать?
    # del lst[i] или lst.pop(i)
    # мне не нравится в данном случае for, но можно попробовать
    # sb: написал сразу 2 строки, собственно append мой, pop твой
    for i in range(0, len(lst)):
        if lst[i] == 0:
            counter_0 += 1
            lst.pop(i)
            lst.append()




    return lst

arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(move_zeros(arr))