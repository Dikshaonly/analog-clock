import numpy as np 
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.animation import FuncAnimation
from datetime import datetime 
fig= plt.figure(figsize=(2.5,2.5),dpi=100)
ax = fig.add_subplot(111, polar=True)
def update(now): 
    plt.cla() # Clear the current figure
    plt.setp(ax.get_yticklables(),visible=False)
    ax.set_xticks(np.linespace(0,2*pi,12,endpoint=False))
    ax.set_xticklables(range(1,13))
    ax.set_theta_direction(-1)
    ax.set_theta_offset(pi/3.0)
    ax.grid(False)
    plt.ylim(0,1)
    now=datetime.now()
    hour=now.hour 
    minute=now.minute
    second=now.second
    angles_h =2*pi*hour/12+2*pi*minute/(12*60)+2*second/(12*60*60)-pi/6.0
    angles_m= 2*pi*minute/60+2*pi*second/(60*60)-pi/6.0
    angles_s =2*pi*second/60-pi/6.0
    ax.plot([angles_s,angles_s], [0,0.9], color="yellow", linewidth=1)
    ax.plot([angles_m,angles_m], [0,0.7], color="black", linewidth=2)
    ax.plot([angles_h,angles_h], [0,0.3], color="black", linewidth=4)
    return ax
ani = FuncAnimation(fig,update, interval = 100)
plt.show()

    
    