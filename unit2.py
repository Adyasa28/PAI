import numpy as np
a=np.array([10,20,30]) #create numpy array
print(type(a))
b=np.array((10,20,30))
print(type(b))
c=np.array([[10,20,30],[40,50,60]])
#ndim
print("a.ndim",a.ndim)
print("c.ndim",c.ndim)

#shape
x=np.array([1,2,3,4,5])# 1D array
y=np.array([
    [1,2,3],
    [4,5,6]
])#2D array
z=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])#3D array

#shape
print("x.shape",x.shape)
print("y.shape",y.shape)
print("z.shape",z.shape)

#size
print("x.size",x.size)
print("y.size",y.size)
print("z.size",z.size)


#dtype
print("x.dtype",x.dtype)
print("y.dtype",y.dtype)
print("z.dtype",z.dtype)

#itemsze
print("x.itemsize",x.itemsize)
print("y.itemsize",y.itemsize)
print("z.itemsize",z.itemsize)

#nbytes
print("x.nbytes",x.nbytes)
print("y.nbytes",y.nbytes)
print("z.nbytes",z.nbytes)
