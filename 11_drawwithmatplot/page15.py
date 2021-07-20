from matplotlib import pyplot as plt
import numpy as np

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

plt.figure(figsize=(15, 8), dpi=80)


_xticks_lables = (i / 2 for i in range(4, 50))
plt.xticks(x)
# 绘制图片
plt.plot(x, y)
# 展示图片
plt.show()
