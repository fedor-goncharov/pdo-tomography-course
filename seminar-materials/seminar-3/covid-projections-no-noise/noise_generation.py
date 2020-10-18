import os
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    observation_time = 1
    intensity_strong = 1e5
    intensity_weak = 5.0 * 1e2
    scatter = 0

    files_list = []
    for file in os.listdir("./"):
        if file.endswith(".bin"):
            files_list.append(file)

    for file in files_list:
        projection_data = np.reshape(
            np.fromfile(file, dtype=np.float), (512, 512))
        prob_projection_data = np.exp(-projection_data /
                                      np.max(projection_data[:]))

        projection_data_strong = np.random.poisson(
            observation_time * (intensity_strong * prob_projection_data + scatter))
        output_strong = "../covid-counts-high-intensity/" + "strong-int-" + file
        np.reshape(projection_data_strong, (512*512)
                   ).astype('float').tofile(output_strong)
        # plt.imshow(projection_data_strong)
        # plt.colorbar()
        # plt.show()

        # generate weak Poisson data
        projection_data_weak = np.random.poisson(
            observation_time * (intensity_weak * prob_projection_data + scatter))
        output_weak = "../covid-counts-low-intensity/" + "weak-int-" + file
        np.reshape(projection_data_weak, (512*512)
                   ).astype('float').tofile(output_weak)
        print(f"File {file} processed.")
        # plt.imshow(projection_data_weak)
        # plt.colorbar()
        # plt.show()
