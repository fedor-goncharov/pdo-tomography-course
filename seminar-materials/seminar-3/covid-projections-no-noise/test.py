import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import iradon, iradon_sart

# read binary and plot projection data

if __name__ == "__main__": 

	data = np.reshape(np.fromfile("proj-covid-data_100.bin", dtype=np.float), (512, 512))
	plt.imshow(data)
	plt.show()
	reconstruction = iradon(data, theta=np.linspace(0, 360, 512, endpoint=False))
	plt.imshow(reconstruction)
	plt.colorbar()
	plt.show()
	