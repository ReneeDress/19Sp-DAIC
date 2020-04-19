import numpy as np
import matplotlib.pyplot as plt
# 模拟每步游走方向
# 将随机游走的步数增加到100步
steps = 100
for i in range(0,50):
    rndwlk = np.random.randint(0, 2, size = (2, steps))
    rndwlk = np.where( rndwlk > 0, 1, -1)
    # 计算每部游走后的位置
    position = rndwlk.cumsum(axis = 1)
    # 计算每步游走后到原点的距离
    dists = np.sqrt(position[0]**2 + position[1]**2)
    np.set_printoptions(precision = 4)
    print("物体到原点的最大距离：", dists.max())
    print("物体到原点的最小距离：", dists.min())
    # 计算物体最终到原点的距离
    finaldists = np.sqrt(position[0,-1]**2 + position[1,-1]**2)
    print("物体最终到原点的距离：", finaldists)
    # 物体到原点距离的变化趋势
    x = np.arange(1,steps+1)
    y = dists
    plt.ylim(0, 50)
    plt.plot(x, y, c='g', marker='*')
    plt.scatter(0, 0, c='r', marker='o')
    plt.text(.1, -.1, 'origin')
    plt.show()