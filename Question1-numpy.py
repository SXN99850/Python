
import numpy as np

#Using numpy we created an array with 15 random elements
random_array = np.random.randint(1,20,15)
print("Random array with numbers in the range [1,20]: \n", random_array)

#Reshape the array to 3 by 5
reshaped_array = np.reshape(random_array, [3, 5])
print("Reshaped array: \n", reshaped_array)
print("Shape: ", reshaped_array.shape)

#Replace the max in each row by 0
max_index = reshaped_array.argmax(axis=1)
print(max_index)
for i in range(0,3):
    reshaped_array[i][max_index[i]] = 0

print("Replacing max in each row by 0 \n", reshaped_array)