import numpy as np
# 模拟每步游走方向
steps = 10
rndwlk = np.random.normal(0, 1, size = (3, steps))
# 计算每步走完后物体在三维空间的位置
position = rndwlk.cumsum(axis = 1)
print("每步走完后物体在三维空间的位置：\n", position)
# 计算每步走完后物体到原点的距离（只显示两位小数）
dists = np.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
np.set_printoptions(precision = 2)
print("每步走完后物体到原点的距离（只显示两位小数）：", dists)
# 统计物体在z轴上到达的最远距离
print("物体在z轴上到达的最远距离：", abs(position[2]).max())
# 统计物体在三维空间距离远点的最近值
print("物体在三维空间距离远点的最近值：", dists.min())