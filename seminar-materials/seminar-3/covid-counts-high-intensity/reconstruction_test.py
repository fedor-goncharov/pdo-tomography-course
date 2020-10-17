import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import iradon

# read binary and plot projection dati
if __name__ == "__main__": 

	intensity = 1e5
	scatter = 0
	data = np.reshape(np.fromfile("strong-int-proj-covid-data_100.bin", dtype=np.float), (512, 512))
	projection_data = -np.log((data - scatter)/(intensity-scatter))
	#projection_data = np.log(projection_data)

	reconstruction = iradon(projection_data, theta=np.linspace(0, 360, 512, endpoint=False))
	plt.imshow(reconstruction.transpose(), cmap = 'gray')
	plt.colorbar()
	plt.title("High count in X-ray image")
	plt.show()