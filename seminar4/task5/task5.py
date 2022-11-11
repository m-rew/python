# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def split_str_poly(line):
    split_line = []
    index1 = 0
    index2 = 0
    i = 0
    while i < len(line):
        index2 = 0

        if index1 == 0 and (line[i] == '+' or line[i] == '-'):
            index2 = i - 1
            split_line.append(line[index1:index2])
            index1 = i
            i = index1

        if index1 != 0 and (line[i] == '+' or line[i] == '-'):
            index1 = i
            for j in range(i + 1, len(line)):
                if line[j] == '+' or line[j] == '-':
                    index2 = j - 1
                    break
                if j == len(line) - 1 and index2 == 0:
                    index2 = j + 1
            split_line.append(line[index1:index2])
            i = index2 + 1
        else:
            i += 1

    return split_line

file1 = open('file1.txt', 'r')
line1 = file1.readline()
file1.close()

print(line1)

split_line = split_str_poly(line1)

print(split_line)