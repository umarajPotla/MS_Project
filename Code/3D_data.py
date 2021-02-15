import numpy as np

d3_array0 = np.array([[[0, 0, 0],[0, 1,0],[0,0,0]],
                     [[0, 1,0],[1,1,1],[0,1,0]],
                     [[0, 0, 0],[0, 1,0],[0,0,0]]
                    ])
                
d3_array1 = np.array([[[0, 1, 0],[0, 1,0],[0,0,0]],
                     [[0, 1,0],[1,1,1],[0,1,0]],
                     [[0, 0, 0],[0, 1,0],[0,1,0]]
                    ])

d3_array2 = np.array([[[0, 1, 0],[0, 1,0],[0,0,0]],
                     [[0, 1,0],[1,1,1],[0,1,0]],
                     [[0, 0, 0],[0, 1,0],[0,1,0]]
                    ])

d3_avg = (d3_array1 + d3_array2)/2

#d3_array = np.concatenate((d3_array1,d3_array2))
d3_array = np.stack((d3_array1,d3_array2))
#print(d3_array.shape)
#print(d3_array)

#print(d3_avg.shape)
#print(d3_avg)
d3_array0 = d3_array0.flatten()
print(d3_array0.shape)
d3_array0 = np.reshape(d3_array0, (1, 27))
print(d3_array0.shape)
print(d3_array0)

d3_array1 = d3_array1.flatten()
print(d3_array1.shape)
d3_array1 = np.reshape(d3_array1, (1, 27))
print(d3_array1.shape)
print(d3_array1)

d3_array2 = d3_array2.flatten()
print(d3_array2.shape)
d3_array2 = np.reshape(d3_array2, (1, 27))
print(d3_array2.shape)
print(d3_array2)
arr_tuple = (d3_array0, d3_array1, d3_array2)

arr = np.vstack(arr_tuple)
print(arr)

sum_arr = np.zeros((3,3,3), dtype=int)
for x in range(3):
    sum_arr = sum_arr + (d3_array+int(x))
print(sum_arr)
avg = sum_arr/3
print(avg)