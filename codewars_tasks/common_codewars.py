# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    # Какой цикл?
    # sb: Было бы неплохо While, но For должен сработать тоже
    # sb: Добавлять в конец - это я помню .append , а как вырезать?
    # del lst[i] или lst.pop(i)
    # мне не нравится в данном случае for, но можно попробовать
    # sb: написал сразу 2 строки, собственно append мой, pop твой
    # OS: так не будет работать, в append() надо в скобках указать что ты добавляеiь.
    # так что либо так: lst.append(lst.pop(i)) или как ниже
    # и что теперь? если принудительно писать сейчас i -= 1, то это очень плохая практика,
    # менять счетчик во время выполнения цикла почти никогда не рекомендуется.
    # У меня опять цейтнот, так что я сделала через while, кодварс принял.
    # Будет оч интересно посмотреть, выпутаешься ли ты с for-ом, а я потом пришлю свой вариант с вайл.
    # Прошу прощения, если это не честно, но времени нет((
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

arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(move_zeros(arr))

# У меня с for не вышло. Но я так его использовать не догадался:
# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array