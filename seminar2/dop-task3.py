# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

some_list1, some_list2 = [1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]
new_list, index_list  = [], []

for i in range(len(some_list1)):
    for j in range(len(some_list2)):
        if some_list1[i] == some_list2[j] and not (j in index_list):
            new_list.append(some_list1[i])
            index_list.append(j)

print(new_list)