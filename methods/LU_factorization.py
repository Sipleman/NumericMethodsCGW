import math


def lu_u(A, b):
    n = len(A[0])
    L = [[0.0 for x in range(n)] for y in range(len(A))]
    U = [[0.0 for x in range(n)] for y in range(len(A))]
    U[0][0] = 1.0
    U[1][1] = 1.0
    U[2][2] = 1.0

    i = 0
    j = 0

    for p in range(n):
        for k in range(j, n):
            sum_tmp = 0
            # for tmp in range(j-2):
            #     sum_tmp += U[tmp][j]*L[i][tmp]
            sum_tmp = sum(U[tmp][j]*L[k][tmp] for tmp in range(len(U)))
            L[k][j] = A[k][j] - sum_tmp

        for k in range(i+1, n):
            tmp_sum = sum(U[tmp][k]*L[i][tmp] for tmp in range(len(U)))
            U[i][k] = 1/L[i][i] * (A[i][k] - tmp_sum)
        i += 1
        j += 1

    y = [0.0]
    for i in range(n):
        print sum(L[i][tmp]*y[tmp] for tmp in range(i))
        tmp = 1/L[i][i] * (b[i] - sum(L[i][tmp]*y[tmp] for tmp in range(i)))
        if i == 0:
            y[0] = tmp
        else:
            y.append(tmp)

    print L
    print U

    x = [0.0, 0.0, 0.0]
    for i in range(n-1, -1, -1):
        tmp = y[i] - sum(U[i][tmp]*x[tmp] for tmp in range(i+1, n))
        x[i] = tmp
    print x