import random

# Генератор квадратной матрицы заданной размерности (случайные числа)
def generate_random_matrix(n):
    arr = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
    return arr


# Генератор квадратной матрицы заданной размерности (последовательные числа)
def generate_matrix(n):
    arr = [[(i * n + j) % 21 - 10 for j in range(n)] for i in range(n)]
    return arr


# Вывод матрицы на экран
def print_matrix(arr, message=None):
    if message:
        print(message)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if isinstance(arr[i][j], float):
                print(f"{round(arr[i][j], 2):6} ", end='')
            else:
                print(f"{arr[i][j]:6} ", end='')
        print()
    print()


# Копирование матрицы
def copy_matrix(arr):
    n = len(arr)
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[i][j]
    return new_arr


# Подсчет количества чисел (в четных столбцах подматрицы E), больших k
def get_first_num(arr, k):
    n = len(arr)
    s = 0
    for i in range(n):
        for j in range(n):
            if (j + 1) % 2 == 0 and arr[i][j] > k:
                s += 1
    return s


# Вычисление суммы чисел в нечетных строках подматрицы E
def get_second_num(arr):
    n = len(arr)
    s = 0
    for i in range(n):
        for j in range(n):
            if (i + 1) % 2 == 1:
                s += arr[i][j]
    return s


# Симметрично меняем местами подматрицы C и E в матрице F
def symmetric_change_C_and_E(F):
    n = len(F)
    for i in range(n // 2):
        for j in range(n // 2):
            p = n - 1 - i
            q = n - 1 - j
            F[i][j], F[p][q] = F[p][q], F[i][j]


# Несимметрично меняем местами подматрицы B и C в матрице F
def non_symmetric_change_B_and_C(F, B, C):
    for i in range(m):
        for j in range(m):
            F[i][n - 1 - j] = C[i][m - 1 - j]
            F[n - 1 - i][n - 1 - j] = B[m - 1 - i][m - 1 - j]


# Транспонирование матрицы
def transpose_matrix(arr):
    n = len(arr)
    new_arr = [[arr[j][i] for j in range(n)] for i in range(n)]
    return new_arr


# Умножение матрицы на число
def scale_matrix(arr, k):
    n = len(arr)
    new_arr = [[arr[i][j] * k for j in range(n)] for i in range(n)]
    return new_arr


# Сложение двух матриц
def add_matrices(arr1, arr2):
    n = len(arr1)
    new_arr = [[arr1[i][j] + arr2[i][j] for j in range(n)] for i in range(n)]
    return new_arr


# Умножение двух матриц
def multiply_matrices(arr1, arr2):
    n = len(arr1)
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                new_arr[i][j] += arr1[i][r] * arr2[r][j]
    return new_arr


# Вычисление определителя матрицы
def determinant(arr):
    def get_sub_array(arr, n, s):
        sub_arr = [[0 for j in range(n - 1)] for i in range(n - 1)]
        for i in range(1, n):
            k = 0
            for j in range(n):
                if j != s:
                    sub_arr[i - 1][k] = arr[i][j]
                    k += 1
        return sub_arr

    n = len(arr)
    result = 0
    if n == 1:
        result = arr[0][0]
    else:
        for i in range(n):
            a = arr[0][i]
            sub_arr = get_sub_array(arr, n, i)
            det = determinant(sub_arr)
            result += pow(-1, i) * a * det
    return result


# Вычисление суммы диагональных элементов матрицы
def diagonal_elements_sum(arr):
    n = len(arr)
    s = 0
    for i in range(n):
        s += arr[i][i]
    return s


# Формирование нижней диагональной матрицы
def low_diagonal_matrix(arr):
    n = len(arr)
    res = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            res[i][j] = arr[i][j]
    return res


# Вычисление обратной матрицы
def inverse_matrix(arr, arr_name):
    def get_matrix_minor(arr, i, j):
        return [row[:j] + row[j + 1:] for row in (arr[:i] + arr[i + 1:])]

    det = determinant(arr)
    if det == 0:
        print(f"Ошибка! Определитель матрицы {arr_name} нулевой, обратная матрица не существует!!!")
        exit(1)
    if len(arr) == 2:
        return [[arr[1][1] / det, -1 * arr[0][1] / det],
                [-1 * arr[1][0] / det, arr[0][0] / det]]

    cofactors = []
    for r in range(len(arr)):
        cofactorRow = []
        for c in range(len(arr)):
            minor = get_matrix_minor(arr, r, c)
            cofactorRow.append(((-1) ** (r + c)) * determinant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    return cofactors

# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ
# Цикл для ввода K
while True:
    try:
        k = int(input("Введите K:\n"))
        break
    except:
        print("Неверный ввод, нужно ввести целое число")

# Цикл для ввода N
while True:
    try:
        n = int(input("Введите размерность N матрицы A (натуральное четное число):\n"))
        if 1 <= n <= 100:
            if not n % 2:
                break
            else:
                print("Нужно ввести четное число")
        elif n > 100:
            print("Слишком большая размерность")
        else:
            print("Недопустимая размерность")
    except:
        print("Неверный ввод, нужно ввести натуральное четное число")


A = generate_random_matrix(n)                       # Генеририуем случайную матрицу
#A = generate_matrix(n)                              # Генеририуем матрицу, элементы которой последовательно увеличиваются
print_matrix(A, "\nСгенерированная матрица A:")     # Вывод матрицы на экран

m = n // 2                                          # Размерность подматриц
B = [[0] * m for _ in range(m)]                     # Для всех 4х подматриц иниициализируем списки
C = [[0] * m for _ in range(m)]
D = [[0] * m for _ in range(m)]
E = [[0] * m for _ in range(m)]

# Все 4 подматрицы
for i in range(m):
    for j in range(m):
        B[i][m - 1 - j] = A[i][n - 1 - j]
        C[m - 1 - i][m - 1 - j] = A[n - 1 - i][n - 1 - j]
        D[m - 1 - i][j] = A[n - 1 - i][j]
        E[i][j] = A[i][j]

# Вывод подматриц на экран
print_matrix(B, "\nМатрица B:")
print_matrix(C, "\nМатрица C:")
print_matrix(D, "\nМатрица D:")
print_matrix(E, "\nМатрица E:")

# Для дальнейшей работы копируем матрицы
F = copy_matrix(A)
E2 = copy_matrix(E)

num1 = get_first_num(E, k)          # Количество чисел (в четных столбцах подматрицы E), больших k
num2 = get_second_num(E)            # Сумма чисел в нечетных строках подматрицы E
print(f"\n\n\nКоличество чисел (в четных столбцах подматрицы E), больших k: {num1}")
print(f"Сумма чисел в нечетных строках подматрицы E: {num2}")

# Сравниваем полученные числа
# Первый случай
if num1 > num2:
    symmetric_change_C_and_E(F)                 # Симметрично меняем местами подматрицы C и E в матрице F
    print("Первое число больше, поэтому симметрично меняем местами подматрицы C и E в матрице F")
# Второй случай
else:
    non_symmetric_change_B_and_C(F, B, C)       # Несимметрично меняем местами подматрицы B и C в матрице F
    print("Первое число не больше, поэтому несимметрично меняем местами подматрицы B и C в матрице F")

print_matrix(F, "Получаем следующую матрицу F:")


det = determinant(A)                            # Определитель матрицы A
diag_sum = diagonal_elements_sum(F)             # Сумма диагональных элементов матрицы F
print(f"\n\n\nОпределитель матрицы A: {det}")
print(f"Сумма диагональных элементов матрицы F: {diag_sum}")

# Сравниваем определитель и указанную сумму
# Первый случай
if det > diag_sum:
    # Вычисляем (A * A^T) – (K * F^Т)
    A_T = transpose_matrix(A)
    F_T = transpose_matrix(F)
    AAT = multiply_matrices(A, A_T)
    KFT = scale_matrix(F_T, -k)
    result = add_matrices(AAT, KFT)

    print_matrix(A_T, "Транспонированная матрица A_T")
    print_matrix(F_T, "Транспонированная матрица F_T")
    print_matrix(AAT, "Произведение A и A_T")
    print_matrix(KFT, "Произведение матрицы F_T на -k")
    print_matrix(result, "Итоговая матрица")
# Второй случай
else:
    # Вычисляем (A^Т + G^-1 - F^-1) * K
    A_T = transpose_matrix(A)
    F_I = inverse_matrix(F, "F")
    G = low_diagonal_matrix(A)
    G_I = inverse_matrix(G, "G")
    temp1 = add_matrices(A_T, G_I)
    temp2 = scale_matrix(F_I, -1)
    temp3 = add_matrices(temp1, temp2)
    result = scale_matrix(temp3, k)

    print_matrix(A_T, "Транспонированная матрица A_T")
    print_matrix(F_I, "Обратная матрица F_I")
    print_matrix(G, "Нижняя диагональная матрица G, полученная из A")
    print_matrix(G_I, "Обратная матрица G_I")
    print_matrix(temp1, "Сумма матриц A_T и G_I")
    print_matrix(temp3, "Разность полученной матрицы и F_I")
    print_matrix(result, "Итоговая матрица")
