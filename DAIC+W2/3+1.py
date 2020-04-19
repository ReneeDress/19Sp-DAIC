import numpy as np
import matplotlib.pyplot as plt
# 模拟每步游走方向
# 将随机游走的步数增加到100步
steps = 100
rndwlk = np.random.randint(0, 2, size = (2, steps))
print(rndwlk)
rndwlk = np.where( rndwlk > 0, 1, -1)
print(rndwlk)
# 计算每部游走后的位置
position = rndwlk.cumsum(axis = 1)
print(position)
# 计算每步游走后到原点的距离
dists = np.sqrt(position[0]**2 + position[1]**2)
print(dists)
np.set_printoptions(precision = 4)
print(dists)
# 计算物体最终到原点的距离
finaldists = np.sqrt(position[0,-1]**2 + position[1,-1]**2)
print("物体最终到原点的距离：", finaldists)
# 绘图展示游走轨迹
x = position[0]
y = position[1]
plt.plot(x, y, c='g', marker='*')
plt.scatter(0, 0, c='r', marker='o')
plt.text(.1, -.1, 'origin')
plt.scatter(x[-1], y[-1], c='r', marker='o')
plt.text(x[-1]+.1, y[-1]-.1, 'stop')
plt.show()