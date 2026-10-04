import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix = np.array(matrix,dtype=np.float64)
    det_matrix = np.linalg.det(matrix)
    if det_matrix == 0 :
        return None
    matrix_inverse = np.linalg.inv(matrix)
    return_list = matrix_inverse.tolist()
    return return_list
        
   
