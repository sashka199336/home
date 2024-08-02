def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите кол-во строк:'))
m = int(input('Введите  кол-во столбцов :'))
value = input(f'Задайте число: ')
matrix = get_matrix(n, m, value)
if n <= 0:
    print("Не верное число:", n)
elif m <=0:
    print("Не верное число:" ,m)

    for i in matrix:
        print(i)
