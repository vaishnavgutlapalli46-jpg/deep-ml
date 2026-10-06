import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b) :
		return -1
	a = np.array(a,dtype = np.float64)
	b =np.array(b,dtype = np.float64)
	return a + b
	
	