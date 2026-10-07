import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float] :
	matrix = np.array(matrix,dtype = np.float64)
	trace = 0 
	for i in range(np.shape(matrix)[0]) :
		trace += matrix[i,i]
	return (np.linalg.det(matrix), trace)
	