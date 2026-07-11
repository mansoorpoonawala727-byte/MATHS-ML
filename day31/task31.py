import numpy as np
packet=np.array([1500,4444,12.0])
print("packet:",packet)
print("shape:",packet.shape)
print("dimensions:",packet.ndim)
traffic=np.array([
     [1500, 4444, 12.0],
    [300, 80, 0.5],
    [1200, 1337, 8.3]
])
print("Matrix:\n", traffic)
print("Shape:", traffic.shape)
print("Dimensions:", traffic.ndim)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.add(a,b))
print(np.multiply(a,b))
print(np.dot(a,b))
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.matmul(A, B))