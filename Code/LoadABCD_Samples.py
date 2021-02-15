import os
import fnmatch
import shutil
import numpy as np
from nibabel.testing import data_path
import nibabel as nib

i = 0
sum_data = np.zeros((121,145,121),dtype=float)
#d3_array = np.zeros(2122945,dtype=float)
for path,dirs,files in os.walk('/Users/umarajpotla/Downloads/Important/MS_Project/Code/ABCD_Data'):
    for file in files:
        if fnmatch.fnmatch(file,'*.nii'):
            #i = i + 1
            sample_abcd_path = os.path.join(path,file)
            #print(sample_abcd_path)
            img = nib.load(sample_abcd_path)
            #print('Image Shape::', img.shape)
            data = img.get_fdata()
            
            sum_data = sum_data + data
            #newPath = shutil.copy(fullname, '/Users/umarajpotla/Downloads/Important/MS_Project/Code/ABCD_Data/Sm6mwc1pT1_'+str(i)+'.nii')
            #print(newPath)
mask = sum_data / 201
print(mask.shape)
mask = mask.flatten()
mask = np.reshape(mask, (1, 2122945))

filter_mask = mask > 0.1
print(filter_mask.shape)
print(filter_mask.dtype)

abcd_sample126_file = os.path.join('/Users/umarajpotla/Downloads/Important/MS_Project/Code/ABCD_Data','Sm6mwc1pT1_126.nii')
abcd_126img = nib.load(abcd_sample126_file) #load 126 image
abcd_126data = abcd_126img.get_fdata() # Get 126 image data

#Flatten and reshape 126 image data
abcd_126data = abcd_126data.flatten()
abcd_126data = np.reshape(abcd_126data, (1, 2122945))

#filter abcd 126 image data with mask
abcd_126_filtered = abcd_126data[filter_mask]
print(abcd_126_filtered.shape)
print(abcd_126_filtered)





