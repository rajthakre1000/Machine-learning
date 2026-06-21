# Tensor is a data structure
# basic data structure of ML
# Tensor flow(google ) 

# Numpy array (tensor)
# [1,2,3,4,6] ==> 1D Tensor/vector (1D/one axis)
# arr.ndim : gives vector(ex: (12,2))
# here 1D Tensor is a vector but dimention of vector is 5D
# 
# 2D Tensor
# [[1,2,3][3,4,5][5,6,7] ]
import numpy as np
temprature = np.array ([20,33,43,12,28,69,5,21])        #1D tensor
print(temprature)

b = np.array([[2,3,4], [5,6,7]])        #2D tensor (2*2)
print(b)

#0-5D tensors are used in ML
# no. of axis = rank= no. of dimention

#1D tensor:
# student(1000)
#               cgpa  iq  state  placement
# 1st student : 8.1   96  wb     1
# 1d tensor= [8.1,96,0,1] (here letting wb=0)
# axis are: 4  

#2D tensor 
# collection of 1d tensors
# 2*2 matrix
# here [[...............]
#       [...............]
#       [...............]] 

#3d tensor
# NLP (Natural Language Processing)/ RGB (color image) /Time series data

# Hi | Nitish | rahul | Ankit
# 1    0        0       0 
# 0    1        0       0
# 0    0        1       0
# 0    0        0       1
# Hi Nitish [[1,0,0,0][0,1,0,0]] (2d)
# Hi Rahul  [[......][........]] (2d)
# HI Ankit                       (2d)
# set of 2d tensors is a 3D tensor

# 4D tensor
# RGB (color image)
# set of 2d tensors = 3d tensor(3,1200,800)         3d tensor
# set of RGB images = 4d tensor (50,3,1200,800)     50 RGB images

#5D tensor
# Videos of multiple frames 
# 60 sec, 30fps, 480*720 (3 channels)
#  (1800,480,720,3)  4d tensor
# multiple videos/ collection of video ==> 5d tensor
