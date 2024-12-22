def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input("Дайти строк матрице: "))
m = int(input("Дайти столбцов матрице: "))
value = input("Дайти значений матрице: ")
print('-----' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print("Матриц пуст, неверное количество строк:", n)
elif m <=0:
    print("Матриц пуст, задано неверное количество столбцов:" ,m)
else:
    print("Встречайте Матриц:")
    for i in matrix:
        print(*i)