import numpy as np

# array=np.array('A')  # 0 dimention 
# array=np.array(['A','B','C'])  # 1 dimention
# array=np.array([['A','B','C'],['A','B','C']]) # 2 dimention
array=np.array([['A','B','C'],['D','E','F'],['G','H','I']])
# for two simensional array
# use array.ndim =number of dimention
#use a.shape to get about number of rows and columns
# a = np.array([
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9],
#         [10,11,12]
#     ]
# ])    #3 dimention
#indexing array[layer,row,column]
#array[row,column]
print(array[2][0])