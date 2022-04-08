import numpy as np

u=np.zeros((101,101))
u[50,50]=1

for t in range(200):
    for i in range(1,100):
        for j in range(1,100):
            u[i,j] +=(u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i, j-1] -4*u[i,j])/4.
            
            import matplotlib.pyplot as plt
            from matplotlib import cm
            from mpl_toolkits import mplot3d
            
x=np.linspace(0,1,101)
y=np.linspace(0,1,101)
X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,u,cmap=cm.coolwarm)
plt.show()
   