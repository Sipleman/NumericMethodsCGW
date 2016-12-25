import copy


def gauss_with_selection_by_columns(A, B):
    for i in range(len(B)):
        A[i].append(B[i])
    print A
    n = len(A[0])
    C = copy.deepcopy(A)

    for k in range(n-1):
        for j in range(k, n):
            C[k][j] = A[k][j]/A[k][k]
        for i in range(k+1, n-1):
            print A
            print i, j, k
            for j in range(n):
                C[i][j] = A[i][j] - C[k][j]*A[i][k]
        A = copy.deepcopy(C)

    result = []
    for i in range(len(C)-1, -1, -1):
        sum = 0
        for j in range(i+1, n-1):
            print result[-(j-1)]
            sum += C[i][j] * result[n-j-2]
        result.append(C[i][-1] - sum)
    print result
    return result
