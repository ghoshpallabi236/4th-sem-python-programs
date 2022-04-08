import numpy as np
from scipy .special import hermite
import matplotlib.pyplot as plt
from itertools import cycle

x=np.linspace(-10,10,100)
lines=['-','--','-.',':','..']
linecycler=cycle(lines)

for i in range(2,6):
    plt.plot(x,hermite(i)(x) , lw=2,ls=next(linecycler))
    
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title(['${H}_1$','${H}_2$','${H}_3$','${H}_4$'],fontsize=15)
plt.title('Hermite Polynomial',size=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()