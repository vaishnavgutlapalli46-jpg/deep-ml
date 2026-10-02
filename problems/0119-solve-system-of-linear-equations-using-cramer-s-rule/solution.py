import numpy as np

def cramers_rule(A, b):
    A = np.array(A,dtype = np.float64)
    b = np.array(b , dtype= np.float64)
   
    det_A = np.linalg.det(A)
    if det_A == 0 :
        return -1
    n = A.shape[0]
    x = np.zeros(n)
    
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b        
        x[i] = np.linalg.det(A_i) / det_A
    
    return x.tolist()