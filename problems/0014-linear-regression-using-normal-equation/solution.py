import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X,dtype=np.float64)
	y = np.array(y,dtype=np.float64)
	XT = X.T
    theta = np.linalg.inv(XT @ X) @ XT @ y
    
    theta = np.round(theta, 4)
    return theta.tolist()
	