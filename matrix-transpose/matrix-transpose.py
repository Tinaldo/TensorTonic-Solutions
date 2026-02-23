import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    rows, columns = A.shape
    
    B = np.zeros((columns, rows))

    for i in range(rows):
        for j in range(columns):
            B[j][i] = A[i][j]

    return B

        
    
