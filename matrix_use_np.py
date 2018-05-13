"""
Библиотека для работы с матрицами на языке Python

Влад Иванов, Дарья Телегина, Никита Рамм
Санкт-Петербург, Университет ИТМО, 2018

"""

import numpy as np

# подключение модуля numpy, потому что глупо и бессмысленно игнорировать технологический прогресс


def td_array(m, n):  # функция для создания пустого двумерного массива
    temp = []
    for i in range(0, m):
        temp.append([])
        for j in range(0, n):
            temp[i].append(0)
    return temp


def to_m(td):  # функция конвертации двумерного массива в тип matrix
    temp = MatrixNP(len(td), len(td[0]))
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


class MatrixNP:  # главный гость сегодняшнего вечера
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

    def __pow__(self, num):
        return to_m(np.linalg.matrix_power(self.table, num))

    def __mul__(self, other):
        temp = self
        if is_num(other):
            for i in range(0, self.m):
                for j in range(0, self.n):
                    temp.table[i][j] = temp.table[i][j] * other
        else:
            temp = to_m(np.matmul(self.table, other.table))
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
        self.table[i - 1][j - 1] = val

    def det(self):  # определитель матрицы
        return np.linalg.det(self.table)

    def inv(self):  # обратная матрица без изменения самой матрицы данного экземпляра класса
        return to_m(np.linalg.inv(self.table))

    def inv_me(self):  # обратная матрица с изменением матрицы данного экземпляра класса
        self.table = np.linalg.inv(self.table)
        return self

    def rank(self):  # ранг матрицы
        return np.linalg.matrix_rank(self.table)

    def T(self):  # транспонирование матрицы без изменения самой матрицы данного экземпляра класса
        return to_m(np.transpose(self.table))

    def T_me(self):  # транспонирование матрицы с изменением матрицы данного экземпляра класса
        self.table = np.transpose(self.table)
        return self



def is_watchable(A, C):  # проверка матрицы на наблюдаемость
    N = A.n
    Wnab = MatrixNP(N, N)
    for i in range(0, N):
        Wnab[i] = to_row(C * (A ** i))
    is_w = True if Wnab.rank() == N else False
    return Wnab, is_w


def is_controllable(A, B):  # проверка матрицы на управляемость
    N = A.m
    Wupr = MatrixNP(N, N)
    for i in range(0, N):
        Wupr[i] = to_col(((A ** i) * B))
    Wupr = Wupr.T()
    is_u = True if Wupr.rank() == N else False
    return Wupr, is_u
