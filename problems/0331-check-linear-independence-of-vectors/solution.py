import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    if not vectors:
        return True
        
    matrix = np.array(vectors, dtype=np.float64)
    num_vectors, dimensions = matrix.shape
    if num_vectors > dimensions:
        return False
    return int(np.linalg.matrix_rank(matrix)) == num_vectors
