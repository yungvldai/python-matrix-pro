"""
ПрОдВиНуТаЯ Библиотека для работы с матрицами на языке Python

Влад Иванов, Дарья Телегина, Никита Рамм
Санкт-Петербург, Университет ИТМО, 2018

"""

# подключение модуля numpy, потому что глупо и бессмысленно игнорировать технологический прогресс


def td_array(m, n):  # функция для создания пустого двумерного массива
    temp = []
    for i in range(0, m):
        temp.append([])
        for j in range(0, n):
            temp[i].append(0)
    return temp


def to_m(td):  # функция конвертации двумерного массива в тип matrix
    temp = Matrix(len(td), len(td[0]))
    for i in range(0, temp.m):
        for j in range(0, temp.n):
            temp[i][j] = td[i][j]
    return temp


def to_row(mat):  # конвертация списка в строку матрицы
    return mat[0]


def to_col(mat):  # конвертация списка в столбец матрицы
    return mat.T()[0]


def is_num(any):  # проверка на число
    try:
        float(any)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def table2str(t_obj):
    to_print = ""
    for j in range(0, len(t_obj)):
        to_print += ' '.join(str(i) for i in t_obj[j])
        to_print += "\n"
    return to_print


def matmul(m1, m2):
    m3 = td_array(len(m1), len(m1[0]))
    s = 0
    if len(m1[0]) != len(m2):
        return m3

    for k in range(0, len(m1)):
        for j in range(0, len(m2[0])):
            for i in range(0, len(m1[0])):
                s = s + (m1[k][i] * m2[i][j])
            m3[k][j] = s
            s = 0

    return m3


def getmm(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getdet(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getdet(getmm(m, 0, c))
    return determinant


def mattrans(a):
    b = td_array(len(a[0]),len(a))
    for m in range(len(a[0])):
        for n in range(len(a)):
            b[m][n] = a[n][m]
    return b


def matrank(a):
    r = 1
    q = 1
    i = len(a)
    j = len(a[0])
    while q <= min(i, j):
        t = td_array(q, q)
        for k in range(0, i - q + 1):
            for l in range(0, j - q + 1):
                for m in range(0, q):
                    for n in range(0, q):
                        t[m][n] = a[k + m][l + n]
                if getdet(t) != 0:
                    r = q
        q += 1
    return r


class Matrix:  # главный гость сегодняшнего вечера
    """
    Конструктор. Он в какой-то степени перегружен: есть два режима работы.

    - считать матрицу из файла
    - создать пустую матрицу N x M

    """
    def __init__(self, filename_or_m, n=-1):
        if n == -1:
            file = open(filename_or_m)
            contents = file.readlines()
            self.m = len(contents)
            self.n = len(contents[0].split(' '))
            self.table = td_array(self.m, self.n)
            for i in range(0, self.m):
                j = 0
                for num in (contents[i]).split(' '):
                    self.table[i][j] = int(num)
                    j += 1
            file.close()
        else:
            self.m = filename_or_m
            self.n = n
            self.table = td_array(filename_or_m, n)

    """
    Перегрузка некоторых операторов
    
    - Beautiful is better than ugly.
    
    """

    def __getitem__(self, index):
        return self.table[index]

    def __setitem__(self, index, value):
        self.table[index] = value

    def __str__(self):
        return table2str(self.table)

    def __pow__(self, pok):
        b = td_array(len(self.table), len(self.table))

        for i in range(0, len(b)):
            b[i][i] = 1

        for i in range(0, pok):
            b = matmul(b, self.table)

        return to_m(b)

    def __mul__(self, other):
        temp = self
        if is_num(other):
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] * other
        else:
            temp = to_m(matmul(self.table, other.table))
        return temp

    def __add__(self, other):
        temp = self
        if is_num(other):
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] + other
        else:
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] + other.table[i][j]
        return temp

    def __sub__(self, other):
        temp = self
        if is_num(other):
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] - other
        else:
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] - other.table[i][j]
        return temp

    def set(self, i, j, val):  # привычное присваивание (работа с матрицами в математике)
        self.table[i][j] = val

    def det(self):  # определитель матрицы
        return getdet(self.table)

    def rank(self):  # ранг матрицы
        return matrank(self.table)

    def T(self):  # транспонирование матрицы без изменения самой матрицы данного экземпляра класса
        return to_m(mattrans(self.table))


def is_watchable(A, C):  # проверка матрицы на наблюдаемость
    N = A.n
    Wnab = Matrix(N, N)
    for i in range(0, N):
        Wnab[i] = to_row(C * (A ** i))
    is_w = True if Wnab.rank() == N else False
    return Wnab, is_w


def is_controllable(A, B):  # проверка матрицы на управляемость
    N = A.m
    Wupr = Matrix(N, N)
    for i in range(0, N):
        Wupr[i] = to_col(((A ** i) * B))
    Wupr = Wupr.T()
    is_u = True if Wupr.rank() == N else False
    return Wupr, is_u
