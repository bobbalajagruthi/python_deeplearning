import numpy as np
arr1=np.array(np.random.randint(low=1, high=20, size=15))
new_matrix=np.reshape(arr1, (3, 5))
print("Random array of size 3 by5 ",new_matrix)
final_matrix=[]
for i in range (0,3):
    x=new_matrix[i].max()
    final_matrix.append(list(np.where(new_matrix[i]==x,0,new_matrix[i])))
print("Output array",np.array(final_matrix))


