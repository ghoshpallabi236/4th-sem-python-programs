import numpy as np
T0=1
L=1

x=np.linspace(0,L,101)
u=T0*np.ones(101)
u[0],u[100]=0,0
for j in range(100):
    u[1:-1] +=0.25*(u[2:]-2*u[1:-1] +u[:-2])
    
    t=1.0/400
    f=lambda m: 4*T0/(np.pi*(2*m-1))*np.sin((2*m-1)*np.pi*x/L)*np.exp(-((2*m-1)*np.pi/L)**2*t)
    exact=sum([f(m)for m in range(1,20)])
    import matplotlib.pyplot as plt
    plt.plot(x,u,'o',x,exact,lw=3)