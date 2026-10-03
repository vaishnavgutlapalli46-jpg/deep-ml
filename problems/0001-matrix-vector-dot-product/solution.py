import numpy as np 
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a = np.array(a,dtype = np.float64)
	b = np.array(b,dtype=np.float64)
	if np.shape(a)[1] != len(b):
		return -1
	return np.dot(a,b).tolist()
	