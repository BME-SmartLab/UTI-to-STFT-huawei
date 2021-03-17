import numpy as np
from acl_model import Model
import matplotlib.pyplot as plt
import pickle

# open .om CNN model
device_id = 1
model_path = "UTI_to_STFT_CNN_aipp.om"
model = Model(device_id, model_path, 64, 128)

# load input ultrasound data (grayscale images)
n_lines = 64
n_pixels_reduced = 128
ult_data = np.fromfile('20180223_spkr048_1432.ult128', dtype='uint8')
ult_data = ult_data.reshape(ult_data, (-1, n_lines, n_pixels_reduced))

# restructure input data to 3 channels
ult_data_3d = np.empty((len(ult_data), n_lines, n_pixels_reduced, 3), dtype='uint8')
ult_data_3d[:, :, :, 0] = ult_data
ult_data_3d[:, :, :, 1] = ult_data
ult_data_3d[:, :, :, 2] = ult_data

# predict UTI-to-STFT
melspec_pred_all = np.empty((len(ult_data), 80))
for i in range(len(ult_data)):
    melspec_pred = model.run(ult_data_3d[i])
    melspec_pred_all[i] = melspec_pred[0]

# save predicted mel-spectrogram
plt.figure(figsize=(10,5))
plt.imshow(np.rot90(melspec_pred_all))
plt.gray()
plt.savefig('melspec_pred_all_1432.png')
plt.close()




