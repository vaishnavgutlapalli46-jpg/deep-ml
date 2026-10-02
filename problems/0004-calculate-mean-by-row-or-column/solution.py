import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    shape = list(np.shape(matrix))
    
    if mode == 'row':
        row_mean = []
        for i in range(shape[0]):
            total = 0
            for j in range(shape[1]):
                total += matrix[i][j]
            row_mean.append(total / shape[1])
        return row_mean
    
    elif mode == 'column':
        column_mean = []
        for i in range(shape[1]):
            total = 0
            for j in range(shape[0]):
                total += matrix[j][i]
            column_mean.append(total / shape[0])
        return column_mean