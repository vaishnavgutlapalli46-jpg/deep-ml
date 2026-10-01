import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix = np.array(matrix)
    trace = np.trace(matrix)
    det = np.linalg.det(matrix)
    
    discriminant = trace**2 - 4*det
    sqrt_disc = discriminant**0.5 
    
    eigenvalue_1 = (trace + sqrt_disc) / 2
    eigenvalue_2 = (trace - sqrt_disc) / 2
    
    return [eigenvalue_1, eigenvalue_2]