#NumPy provides a high performance multidiemntional object
#also tools for working with these arrays
import numpy as np
lst=[1,2,3,4,5]
lst1=[1,3,5,7,9]
lst2=[2,4,6,8,0]
arr=np.array(lst)#numpy array is created
print(type(arr))#<class 'numpy.ndarray'>
print(arr)
print(arr.shape)#prints the number of rows and columns
arr1=np.array([lst,lst1,lst2])
print(arr1)
print(arr1.shape)
print(arr1.reshape(5,3))
#indexing:
print(arr[3])
print(arr1[0:2,0:2])#until the 1st row/column
print(arr1[1:,3:])
arr=np.arange(0,10,step=2)#not arrange
print(arr)
print(np.linspace(0,1,10))
#copy() and broadcasting
arr[2:]=100
print(arr)
#this is referencing:
arr2=arr
arr2[2:]=500
print(arr)
print(arr2)
#this changes the values of arr too, we don't want that so we use copy()
arr[2:]=100
arr2=arr.copy()
arr2[2:]=500
print(arr2)
print(arr)
print(arr>2)
print(arr<100)
print(arr[arr<100])
print(arr[arr>2])
print(np.ones((4,4),dtype=int))
print(np.random.rand(3,3)*10)