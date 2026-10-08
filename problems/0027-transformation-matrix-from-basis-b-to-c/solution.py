import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B,dtype=np.float64)
	C = np.array(C,dtype=np.float64)
	C_inverse = np.linalg.inv(C)
	return np.matmul(C_inverse, B).tolist()
	