import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	
	a = np.array(a,dtype=np.float64)
	try :
		return np.reshape(a,new_shape)
	except ValueError:
		return []