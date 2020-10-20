import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
 
 
def chaos(x1):
    """
    :return: 图像
    """
    matplotlib.rcParams['font.sans-serif'] = ['STZhongsong']
    plt.figure(figsize=(12, 9), dpi=80)
    # 开启交互模式
    plt.ion()
    stable_x, stable_y = [], []
    for r in range(1, 1000):
        r /= 200
        x, y, xn = [], [], x1
        for n in range(80):
            xn = r*xn*(1-xn)
            if xn > 1:
                xn = 0.999999
            if xn < 0:
                xn = 0.000001
            y.append(xn)
            x.append(n)
            if n >= 70:
                stable_y.append(xn)
                stable_x.append(r)
        # print(r, y[0:20])
        # Xn-n
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.title("Chaos,xn-n图像")
        plt.grid(True)
        plt.xlabel("n")
        plt.xlim(-1, 80)
        plt.ylabel("Xn")
        plt.ylim(-0.01, 1.01)
        plt.scatter(x, y, marker=".", linewidths=1)
        # Stable-r
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.title("Chaos,stable-r图像")
        plt.grid(True)
        plt.xlabel("r")
        plt.xlim(0, 5.5)
        plt.ylabel("Stable")
        plt.ylim(-0.01, 1.01)
        plt.scatter(stable_x, stable_y, marker=".", linewidths=1)
        plt.pause(0.005)
    # 关闭交互模式
    plt.ioff()
    plt.show()
    return
 
 
if __name__ == "__main__":
    chaos(0.1)
    pass