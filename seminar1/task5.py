# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# (xb - xa)2 + (yb - ya)2

coordinate_first = list(map(int, input('Введите координаты первой точки через запятую: ').replace(" ", "").split(',')))
coordinate_second = list(map(int, input('Введите координаты второй точки через запятую: ').replace(" ", "").split(',')))

x1 = int(coordinate_first[0])
y1 = int(coordinate_first[1])
x2 = int(coordinate_second[0])
y2 = int(coordinate_second[1])

length_line = str(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

length_line = length_line[:length_line.find('.')+3]
print(f'Расстояние между точками в 2D пространстве: {length_line}')