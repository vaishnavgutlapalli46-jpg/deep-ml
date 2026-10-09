import numpy as np
def translate_object(points, tx, ty):
	points = np.array(points,dtype=np.float64)
	translative_result = points + np.array([tx,ty],dtype=np.float64)
	return translative_result.tolist()
	

