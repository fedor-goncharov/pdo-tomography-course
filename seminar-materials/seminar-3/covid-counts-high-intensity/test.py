import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import iradon

# read binary and plot projection dati
if __name__ == "__main__": 

	data = np.reshape(np.fromfile("strong-int-proj-covid-data_0.bin", dtype=np.float), (512, 512))
	
	# test reconstruction 
	intensity_high = 1e5
	projection_data = np.log(intensity_high) - np.log(data)
	reconstruction = iradon(projection_data.transpose(), theta = np.linspace(0, 2*np.pi, 512, endpoint=False))
	plt.imshow(reconstruction)
	plt.colorbar()
	plt.show()
	