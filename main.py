import matrix as mat
import time
import random

random.seed(2018)

N = 200
B = -100
E = 1
M = 5
# A 4x4
# B 4x1
# C 1x4

f = open('A.txt', 'w')
for i in range(0, N):
    f.write(str(random.randint(B, E)) + ' ')
f.close()

f = open('B.txt', 'w')
for i in range(0, N):
    f.write(str(random.randint(B, E)) + ' ')
f.close()

f = open('C.txt', 'w')
for i in range(0, N):
    f.write(str(random.randint(B, E)) + ' ')
f.close()


time.clock()

MAT_A = []
MAT_B = []
MAT_C = []

f = open('A.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_A.append(mat.Matrix(4, 4))
    for k in range(0, 4):
        for j in range(0, 4):
            MAT_A[i].set(k, j, int(buf[(k * 4 + j) + i * 16]))
f.close()

f = open('B.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_B.append(mat.Matrix(4, 1))
    for k in range(0, 4):
        MAT_B[i].set(k, 0, int(buf[k + i * 4]))
f.close()

f = open('C.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_C.append(mat.Matrix(1, 4))
    for j in range(0, 4):
        MAT_C[i].set(0, j, int(buf[j + i * 4]))
f.close()

f = open('result.txt', 'w')

for i in range(0, M):
    f.write("Дано: \n")

    f.write("Матрица системы A" + str(i + 1) + "\n")
    f.write(mat.table2str(MAT_A[i].table))

    f.write("Матрица системы B" + str(i + 1) + "\n")
    f.write(mat.table2str(MAT_B[i].table))

    f.write("Матрица системы C" + str(i + 1) + "\n")
    f.write(mat.table2str(MAT_C[i].table))

    f.write("Проверка на управляемость\n")
    f.write("Матрица управляемости\n")

    Wupr, is_c = mat.is_controllable(MAT_A[i], MAT_B[i])

    f.write(mat.table2str(Wupr.table))
    f.write("Ранг матрицы управляемости: " + str(Wupr.rank()) + "\n")

    if is_c:
        f.write("Матрица управляема")
    else:
        f.write("Матрица неуправляема")

    f.write("\n")

    f.write("Проверка на наблюдаемость\n")
    f.write("Матрица наблюдаемости\n")

    Wnab, is_w = mat.is_watchable(MAT_A[i], MAT_C[i])

    f.write(mat.table2str(Wnab.table))
    f.write("Ранг матрицы управляемости: " + str(Wnab.rank()) + "\n")

    if is_w:
        f.write("Матрица наблюдаема")
    else:
        f.write("Матрица ненаблюдаема")

    f.write("\n\n")

f.close()

print("runtime (own functions): " + str(time.clock()))

import matrix_use_np as matnp

time.clock()

MAT_A = []
MAT_B = []
MAT_C = []

f = open('A.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_A.append(matnp.MatrixNP(4, 4))
    for k in range(0, 4):
        for j in range(0, 4):
            MAT_A[i].set(k, j, int(buf[(k * 4 + j) + i * 16]))
f.close()

f = open('B.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_B.append(matnp.MatrixNP(4, 1))
    for k in range(0, 4):
        MAT_B[i].set(k, 0, int(buf[k + i * 4]))
f.close()

f = open('C.txt', 'r')
buf = f.readline().split(' ')
for i in range(0, M):
    MAT_C.append(matnp.MatrixNP(1, 4))
    for j in range(0, 4):
        MAT_C[i].set(0, j, int(buf[j + i * 4]))
f.close()

f = open('result_use_np.txt', 'w')

for i in range(0, M):
    f.write("Дано: \n")

    f.write("Матрица системы A" + str(i + 1) + "\n")
    f.write(matnp.table2str(MAT_A[i].table))

    f.write("Матрица системы B" + str(i + 1) + "\n")
    f.write(matnp.table2str(MAT_B[i].table))

    f.write("Матрица системы C" + str(i + 1) + "\n")
    f.write(matnp.table2str(MAT_C[i].table))

    f.write("Проверка на управляемость\n")
    f.write("Матрица управляемости\n")

    Wupr, is_c = matnp.is_controllable(MAT_A[i], MAT_B[i])

    f.write(matnp.table2str(Wupr.table))
    f.write("Ранг матрицы управляемости: " + str(Wupr.rank()) + "\n")

    if is_c:
        f.write("Матрица управляема")
    else:
        f.write("Матрица неуправляема")

    f.write("\n")

    f.write("Проверка на наблюдаемость\n")
    f.write("Матрица наблюдаемости\n")

    Wnab, is_w = matnp.is_watchable(MAT_A[i], MAT_C[i])

    f.write(matnp.table2str(Wnab.table))
    f.write("Ранг матрицы управляемости: " + str(Wnab.rank()) + "\n")

    if is_w:
        f.write("Матрица наблюдаема")
    else:
        f.write("Матрица ненаблюдаема")

    f.write("\n\n")

f.close()

print("runtime (NumPy functions): " + str(time.clock()))

