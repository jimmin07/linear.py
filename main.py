#일차함수 그래프 그려줌

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

fig, ax = plt.subplots()

#x, y축 위치 조정
ax.spines['left'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))
ax.tick_params('both', length=0)
plt.yscale('linear')
plt.yscale('linear')

x = np.arange(-5, 5)
m = int(input("기울기: "))
n = int(input("y 절편: "))

y = m*x + n

plt.plot(x,y)

plt.show()

