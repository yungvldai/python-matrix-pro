import numpy as np
import time

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    buf = input().split(' ')
    for j in range(0, 3):
        A[i][j] = int(buf[j])


def td_array(m, n): 
    temp = []
    for i in range(0, m):
        temp.append([])
        for j in range(0, n):
            temp[i].append(0)
    return temp


def mattrans(a):
    b = td_array(len(a[0]),len(a))
    for m in range(len(a[0])):
        for n in range(len(a)):
            b[m][n] = a[n][m]
    return b


def getmm(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getdet(m):
    if len(m) == 1:
        return m[0][0]
    
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    dt = 0
    for c in range(len(m)):
        dt += ((-1) ** c) * m[0][c] * getdet(getmm(m, 0, c))
    return dt


def invmat(m):
    dt = getdet(m)
    if dt == 0:
        return "cannot compute -1 power of matrix due to null determinant"
    if len(m) == 2:
        return [[m[1][1] / dt, -m[0][1] / dt],
                [-m[1][0] / dt, m[0][0] / dt]]

    cfrs = []
    for r in range(len(m)):
        cfrRow = []
        for c in range(len(m)):
            minor = getmm(m, r, c)
            cfrRow.append(((-1)**(r + c)) * getdet(minor))
        cfrs.append(cfrRow)
    cfrs = mattrans(cfrs)
    for r in range(len(cfrs)):
        for c in range(len(cfrs)):
            cfrs[r][c] = cfrs[r][c]/dt
    return cfrs


time.clock()

B = invmat(A)
print("-1 power of matrix computation time (own functions): " + str(time.clock()))

B = np.linalg.inv(A)
print("-1 power of matrix computation time (NumPy functions): " + str(time.clock()))
