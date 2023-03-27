# calculating pi using statistical method
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

def pi_calculator(N):
    cnt=0
    x1,y1,x2,y2=[],[],[],[]
    for i in range(N):
        x_= rnd.random()
        y_= rnd.random()
        if x_**2+y_**2 < 1:
            cnt+=1
            x1.append(x_)
            y1.append(y_)
        else:
            x2.append(x_)
            y2.append(y_)
    plt.scatter(x1,y1,marker='o',color='g',s=8)
    plt.scatter(x2,y2,marker='o',color='r',s=8)
    plt.show()
    return 4*cnt/N

def pi_calculator_np(N):
    x=np.random.random(N)
    y=np.random.random(N)
    inner,outer=[],[]
    for (i,j) in [*zip(x,y)]:
        if i**2+j**2 <1.0:
            inner.append((i,j))
        else:
            outer.append((i,j))
    plt.scatter(*zip(*inner),marker='o',color='g',s=8)
    plt.scatter(*zip(*outer),marker='o',color='r',s=8)
    plt.show()
    return 4*len(inner)/N