import numpy as np

M = float(input('M='))
S = float(input('S='))
NO = int(input('NO='))

R = np.random.rand(9, NO)
N = 0

a = (M * S) ** (1/3)
b = (M / S**2) ** (1/3)

for k in range(NO):
    x0 = a * R[0, k]
    y0 = a * R[1, k]
    z0 = b * R[2, k]
    
    phi1 = 2 * np.pi * R[3, k]
    cthi1 = 2 * R[4, k] - 1
    d1 = R[5, k]
    
    phi2 = 2 * np.pi * R[6, k]
    cthi2 = 2 * R[7, k] - 1
    d2 = R[8, k]
    
    sthi1 = np.sqrt(1 - cthi1**2)
    sthi2 = np.sqrt(1 - cthi2**2)
    
    x1 = x0 + d1 * sthi1 * np.cos(phi1)
    y1 = y0 + d1 * sthi1 * np.sin(phi1)
    z1 = z0 + d1 * cthi1
    
    x2 = x0 + d2 * sthi2 * np.cos(phi2)
    y2 = y0 + d2 * sthi2 * np.sin(phi2)
    z2 = z0 + d2 * cthi2
    
    cond1 = (0 <= x1 <= 1) and (0 <= y1 <= 1) and (0 <= z1 <= 1)
    cond2 = (0 <= x2 <= 1) and (0 <= y2 <= 1) and (0 <= z2 <= 1)
    
    if cond1 or cond2:
        N += 1

f = N / NO
print(f"f = {f}")
