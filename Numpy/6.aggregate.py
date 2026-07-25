import numpy as np 

a=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(np.sum(array))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))