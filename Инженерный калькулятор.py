import math
a = int(input("Выберите тип операции: \n 1 для выбора сложения \n 2 для выбора вычитания \n 3 для выбора умножения \n 4 для выбора деления\n 5 для возведения в степень\n 6 для квадратного корня \n 7 для факториала \n 8 для синуса введенного угла \n 9 для косинуса введенного угла \n 10 для тангенса введенного угла\n"))
if a == 1:
    b = float(input("Введите первое значение\n"))
    c = float(input("Введите второе значение\n"))
    print(b+c)
elif a == 2:
    b = float(input("Введите первое значение\n"))
    c = float(input("Введите второе значение\n"))
    print(b-c)
elif a == 3:
    b = float(input("Введите первое значение\n"))
    c = float(input("Введите второе значение\n"))
    print(b*c)
elif a == 4:
    b = float(input("Введите первое значение\n"))
    c = float(input("Введите второе значение\n"))
    if c == 0:
        c = float(input("Введено некорректное значение, введите новое\n"))
    print(b/c)
elif a == 5:
    b = float(input("Введите число\n"))
    c = float(input("Введите степень\n"))
    print(b**c)
elif a == 6:
    b = float(input("Введите число\n"))
    print(math.sqrt(b))
elif a == 7:
    b = int(input("Введите число\n"))
    print(math.factorial(b))
elif a == 8:
    b = int(input("Введите значение угла\n"))
    sin = math.sin(math.radians(b))
    print(sin)
elif a == 9:
    b = int(input("Введите значение угла\n"))
    cos = math.cos(math.radians(b))
    print(cos)
elif a == 10:
    b = int(input("Введите значение угла\n"))
    tan = math.tan(math.radians(b))
    print(tan)