import numpy as np

X = np.array([3,3],[4,3],[1,1]) #向量
y = np.array([1,1,-1])
w = np.array([0,0])
b = 0
eta = 1
i = 0

for ls in X:
    if y[i]*(ls[0]*w[0]+ls[1]*w[1] + b) <= 0:
        w = w + eta * y[i] * ls
        b = b + eta * y[i]
    i += 1

print(w,b)