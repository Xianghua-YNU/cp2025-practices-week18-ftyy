import numpy as np
import matplotlib.pyplot as plt

# 常数
a = 5.29e-2  # nm
D_max = 1.1
r0 = 0.25  # nm

def D(r):
    """概率密度函数"""
    return 4 * r**2 / a**3 * np.exp(-2 * r / a)

def sample_points(N):
    """接受-拒绝法采样电子位置"""
    points = []
    count = 0
    while len(points) < N:
        r = np.random.uniform(0, r0)
        d = np.random.uniform(0, D_max)
        if d < D(r):
            # 球坐标采样方向
            theta = np.arccos(1 - 2 * np.random.rand())
            phi = 2 * np.pi * np.random.rand()
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            points.append([x, y, z])
        count += 1
        if count > N * 100:  # 防止死循环
            break
    return np.array(points)

if __name__ == "__main__":
    N = 5000  # 采样点数，可调整
    points = sample_points(N)
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], s=1, alpha=0.5)
    ax.set_title("Hydrogen Atom Ground State Electron Cloud")
    ax.set_xlabel("x (nm)")
    ax.set_ylabel("y (nm)")
    ax.set_zlabel("z (nm)")
    plt.show()

    # 分析参数影响
    # 你可以尝试修改N、r0、a等参数，观察电子云分布的变化。
