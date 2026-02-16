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

#Indexing and Slicing

a=np.array([10,20,30,40,50])

#Indexing (Access single element)
print("a[0] :",a[0])
print("a[-1]:",a[-1])
print("a[1]:",a[1])
print("a[-2]:",a[-2])
print("a[2]:",a[2])

#Slicing(Access multiple elements)
#array[start:stop:step]
print("a[1:3]:",a[1:3])
print("a[-3:-1:2]:",a[-3:-1:2])
print("a[ ::-1]:",a[ ::-1])


#Indexing and Slicing in 2D array

b=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#Indexing (Single Element)
print("b[0,0]:",b[0,0])
print("b[0,1]:",b[0,1])
print("b[1,0]:",b[1,0])
print("b[1,2]:",b[1,2])

#Getting Entire row
print("b[1]:",b[1])
print("b[-1]:",b[-1])

#Getting entire column
print("a[:,1] :",a[:,1])

#Slicing
print("b[0:2,0:2] :",b[0:2,0:2])

#Fancy Indexing

a=np.array([10,20,30,40,50,60])

indices=[0,2,4]
b=a[indices]
print("b",b)

#Boolean Masking

mask=(a>30) & (a<40)
print("mask:",mask)
c=a[mask]
print("c",c)

# coat=a<40
# print("coat:",coat)
# d=a[coat]
# print("d",d)

a=np.array([1,2,3])
#b=a[0:3]
b=a[0:3].copy()
print("b:",b)
b[0]=5
print("a:",a)


