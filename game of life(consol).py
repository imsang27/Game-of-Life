import os
import time
import random

W, H = 60, 25          # 격자 크기
P = 0.25               # 초기 생존 확률
FPS = 12               # 초당 프레임

def make_grid(w, h, p):
    return [[1 if random.random() < p else 0 for _ in range(w)] for _ in range(h)]

def count_neighbors(g, x, y):
    h, w = len(g), len(g[0])
    s = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % w
            ny = (y + dy) % h
            s += g[ny][nx]
    return s

def step(g):
    h, w = len(g), len(g[0])
    ng = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            n = count_neighbors(g, x, y)
            if g[y][x] == 1:
                ng[y][x] = 1 if (n == 2 or n == 3) else 0
            else:
                ng[y][x] = 1 if (n == 3) else 0
    return ng

def render(g):
    # Windows에서 깜빡임 줄이려면 cls 사용
    os.system("cls" if os.name == "nt" else "clear")
    # 살아있는 셀: █, 죽은 셀: 공백
    lines = []
    for row in g:
        lines.append("".join("██" if c else "  " for c in row))
    print("\n".join(lines))

def main():
    g = make_grid(W, H, P)
    dt = 1.0 / FPS
    while True:
        render(g)
        g = step(g)
        time.sleep(dt)

if __name__ == "__main__":
    main()
