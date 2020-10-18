import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import iradon

# read binary and plot projection dati
if __name__ == "__main__": 

	intensity = 5*1e2
	scatter = 0
	data = np.reshape(np.fromfile("weak-int-proj-covid-data_1.bin", dtype=np.float), (512, 512))
	projection_data = -np.log((data - scatter)/(intensity))
	#projection_data = np.log(projection_data)
	reconstruction = iradon(projection_data, theta=np.linspace(0, 360, 512, endpoint=False))
	plt.imshow(reconstruction.transpose(), cmap='gray')
	plt.title("Low counts for X-ray image")
	plt.colorbar()
	plt.show()
	
