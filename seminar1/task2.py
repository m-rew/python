# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

i = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not (x or y or z) == (not x) and (not y) and (not z)

            i += 1
            print(f'\n{i} вариация\n')

            print(f'X = {x}; Y = {y}; Z = {z}')
            print(f'    ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
            print(f'    ¬{int((x or y or z))} = {int(not x)} ⋀ {int(not y)} ⋀ {int(not z)}')
            print(f'    {int(not(x or y or z))} = {int((not x) and (not y) and (not z))}')
            print(f'    result = {result}')

            print()
            
            if not(x and y and z):
                print('-' * 40)