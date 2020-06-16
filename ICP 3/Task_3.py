import numpy as np
# get array with size 20
arr1=np.array(np.random.randint(low=1, high=20, size=20))
#Reshaping the array into 4by 5
new_matrix=np.reshape(arr1, (4, 5))
print("Random array of size 4 by 5 ",new_matrix)
#replacing maximum of row with zero
print("output Matrix",np.where(new_matrix == np.max(new_matrix, axis=1, keepdims=True), 0, new_matrix))


