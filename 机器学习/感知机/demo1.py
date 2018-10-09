import numpy as np



X = np.array([[3,3],[4,3],[1,1]]) #多维数组
y = np.array([1,1,-1]) #创建一维数组
w = np.array([0,0])
b = 0
eta = 1

N = 5
n_iter = 0
while(n_iter < N):
    i=0
    for ls in X:

        if y[i]*(ls[0]*w[0]+ls[1]*w[1]+ b) <= 0 :
            w = w + eta*y[i]*ls
            b = b + eta*y[i]

        i=i+1
        
    n_iter = n_iter + 1

print(w,b)


"""完善感知机程序，使它能适应多维数据的学习"""

