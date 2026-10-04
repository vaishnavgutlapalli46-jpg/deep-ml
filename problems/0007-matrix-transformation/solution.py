import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A,dtype=np.float64)
	T = np.array(T,dtype=np.float64)
	S =  np.array(S,dtype=np.float64)
	if np.linalg.det(T)  == 0 or np.linalg.det(S) == 0:
		return -1
	return np.dot(np.dot(np.linalg.inv(T),A),S)
	