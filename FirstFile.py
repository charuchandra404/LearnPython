import numpy as np

arr  = np.array([1,2,3,4,5])
print(arr)

#print(np.__version__)
print(type(arr))

arr1 = np.array(42)
print(arr1)
print('number of dimension: ',arr1.ndim)

arr = np.array((10,20,30))
print(arr)
print('number of dimension: ', arr.ndim)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('number of dimension: ',arr.ndim)

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print('number of dimension: ', arr.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#From both elements, return index 2:
print(arr[0:2,2])

print(arr[0:2, 1:4])

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#view
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
x[0] = 31
print(arr)
print(f'ref obj: {x}')
print(x.base)
#copy
y = arr.copy()
arr[0] = 45
print(arr)
print(y)
print(y.base)

#shape
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('shape of array :',arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print('reshaped 2d:', newarr)
newarr1 = arr.reshape(2, 3, 2)
print('reshaped 3d:', newarr1)

#iteration
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

