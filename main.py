from methods import gauss_with_selection, LU_factorization


if __name__ == "__main__":
    # A = [[3.0, 2.0, 5.0], [4.0, 6.0, 3.0], [6.0, 4.0, 2.0]]
    # B = [-1.0, 2.0, 4.0]
    A = [[3.0, -1.0, 0.0], [-2.0, 1.0, 1.0], [2.0, -1.0, 4.0]]
    B = [5.0, 0.0, 15.0]
    LU_factorization.lu_u(A, B)
