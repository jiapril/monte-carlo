import numpy as np
import matplotlib.pyplot as plt
N=4
x=np.random.random(N)
y=np.random.random(N)
inner,outer=[],[]
for (i,j) in [*zip(x,y)]:
    if i**2+j**2 <1.0:
        inner.append((i,j))
    else:
        outer.append((i,j))
#print(inner)
#print(outer)
plt.scatter(*zip(*inner),marker='o',color='r',s=8)
plt.scatter(*zip(*outer),marker='o',color='r',s=8)
plt.show()