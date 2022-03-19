import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 50)
y = x**4 + 4 * x**3 - 2 * x**2 - 12 * x + 9
y2 = (3 * x**2 + 2) / (x + 2)

if np.any(x) < 0:
    y3 = x**4 + 4 * x**3 - 2 * x**2 - 12 * x + 9
elif np.any(x) <= - 3 or np.any(x) < 0:
    y3 = 9
elif np.any(x) >= 1:
    y3 = (3 * x ** 2 + 2) / (x + 2)


fig, ax = plt.subplots(figsize=(6, 6))



ax.set_title('1 задача')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)


ax.grid(which='major', linewidth=1.2)
ax.grid(which='minor', linestyle='--', color='gray')
plt.plot(x, y, 'r--')


fig, bx = plt.subplots(figsize=(6, 6))

bx.set_title('2 задача')
bx.set_xlabel('x', fontsize=14)
bx.set_ylabel('y', fontsize=14)
bx.grid(which='major', linewidth=1.2)
bx.grid(which='minor', linestyle='-', color='gray')

plt.plot(x, y2, 'r-', color='blue')

fig, cx = plt.subplots(figsize=(6, 6))

cx.set_title('3 задача')
cx.set_xlabel('x', fontsize=14)
cx.set_ylabel('y', fontsize=14)
cx.grid(which='major', linewidth=1.2)
cx.grid(which='minor', linestyle='-', color='gray')

plt.plot(x, y3, 'r-.', color='green')

plt.show()