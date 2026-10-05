import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              a = np.array(a,dtype=np.float64)
              b = np.array(b,dtype=np.float64)
              a_1 = list(np.shape(a))
              b_1= list(np.shape(b))
              if a_1[1] != b_1[0]:
                return -1
              return  np.matmul(a, b).tolist()
	