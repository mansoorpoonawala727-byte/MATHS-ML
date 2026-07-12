import numpy as np
packet=np.array([
    [1200,157,6.0],
    [670,67,6.7],
    [1500,60000,12.0],
    [200,87,2.0]
])
print("SHAPE:",packet.shape)
print("MEAN:",np.mean(packet ,axis=0))
print("HIGHEST ORDER:",np.argmax(np.sum(packet,axis=1)))

X = np.array([
    [1500, 4444, 12.0],
    [300, 80, 0.5],
    [1200, 1337, 8.3]
])

W = np.array([[0.1], [0.2], [0.3]])
predictions=np.matmul(X,W)
print("PREDICTION:",predictions)
print("SHAPE:",predictions.shape)
print("X shape:", X.shape)
print("X transposed shape:", X.T.shape)
print("X transposed:\n", X.T)