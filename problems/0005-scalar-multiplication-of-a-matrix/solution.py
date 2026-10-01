import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
   array = np.array(matrix,dtype=np.float32)
   array = array*scalar
   return array.tolist()
	
    
  