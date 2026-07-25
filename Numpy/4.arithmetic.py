import numpy as np

# scalar arithmetic

array=np.array([1,2,3,4])
a=np.array([5,6,7,8])

# print(array+1)
# print(array-2)
# print(array*3)
# print(array/4)
# print(array**5)


#vectorized math funcs

# print(np.sqrt(array))
# print(np.floor(array))

#element wise arithmetic
# print(array+a)


#comparison operators

scores=np.array([91,55,100,73,82,64])
scores[scores<60]=0
print(scores)