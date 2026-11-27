import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row_size = len(A)
    col_size = len(A[0])
    trans_matrix = [[] for _ in range(col_size)]

    for row_index in range(row_size):
        row = A[row_index]
        for col_index in range(col_size):
            col_num = row[col_index]
            
            trans_matrix[col_index].append(col_num)

    return np.array(trans_matrix)
            
