import numpy as np
def transpose_matrix(matrix):
    matrix = np.array(matrix, dtype=np.float64)
    try:
        return np.transpose(matrix).tolist()
    except ValueError:
        return []
 