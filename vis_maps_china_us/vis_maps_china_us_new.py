import math
import matplotlib.pyplot as plt
import random
def vis_usa_china(N=100):
    r, theta = 0.001, 0
    r_step, theta_step = 0.001, 0.1
    x , y, color_ =[], [], []
#    j = 0
    for i in range(N):
        #if i %(360//theta_step) ==0:
         #   r += j*r_step
         #   j += 1
        r += i*r_step
        theta = (theta+i*(theta_step))%360
        x.append(r*math.cos(theta))
        y.append(r*math.sin(theta))
        color_.append(random.random())
    plt.scatter(x,y,c= color_, alpha = 0.3)
    plt.show()
if __name__ == "__main__":
    vis_usa_china(10000)
