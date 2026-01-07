import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

W, H = 120, 80
P = 0.2          # 초기 생존 확률
INTERVAL_MS = 50 # 프레임 간격

grid = (np.random.rand(H, W) < P).astype(np.uint8)

def step(g: np.ndarray) -> np.ndarray:
    # 토러스 이웃 합: np.roll로 8방향 합산
    n = (
        np.roll(np.roll(g,  1, 0),  1, 1) + np.roll(g,  1, 0) + np.roll(np.roll(g,  1, 0), -1, 1) +
        np.roll(g,  1, 1)                                   + np.roll(g, -1, 1) +
        np.roll(np.roll(g, -1, 0),  1, 1) + np.roll(g, -1, 0) + np.roll(np.roll(g, -1, 0), -1, 1)
    )

    survive = (g == 1) & ((n == 2) | (n == 3))
    born    = (g == 0) & (n == 3)
    return (survive | born).astype(np.uint8)

fig, ax = plt.subplots()
im = ax.imshow(grid, interpolation="nearest")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Conway's Game of Life")

def update(_):
    global grid
    grid = step(grid)
    im.set_data(grid)
    return (im,)

ani = FuncAnimation(fig, update, interval=INTERVAL_MS, blit=True)
plt.show()
