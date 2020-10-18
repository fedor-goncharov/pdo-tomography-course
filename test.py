import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import iradon

# read binary and plot projection dati
if __name__ == "__main__": 


	intensity = 5 * 1e2

	angles = np.linspace(0, 360, 512, endpoint=False)

	data = np.reshape(np.fromfile("weak-int-proj-covid-data_100.bin", dtype=np.float), (512, 512))
	plt.imshow(data)
	plt.colorbar()
	plt.show()

	

