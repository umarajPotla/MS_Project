import os
import numpy as np
from nibabel.testing import data_path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

example_file = os.path.join(data_path, 'example4d.nii.gz')
abcd_sample_file = os.path.join('/Users/umarajpotla/Downloads/Important/MS_Project/Code','Sm6mwc1pT1.nii')
  
import nibabel as nib
img = nib.load(abcd_sample_file)

#print('Image::', img)
print('Image Shape::', img.shape)
#print('Is img data type int16? ', img.get_data_dtype() == np.dtype(np.int16))
#print('Image affine shape::', img.affine.shape)

data = img.get_fdata()
print('Image FData Shape::', data.shape)
print('Type of fdata of image::', type(data))
print(data[100][100][80])

#img_header = img.header
#print('Image header::', img_header)


# Slice 3D data from
#first_vol = data[:, :, :, 0]
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(first_vol)

plt.imshow(data[:, :, 80], cmap='gray')
plt.show()
