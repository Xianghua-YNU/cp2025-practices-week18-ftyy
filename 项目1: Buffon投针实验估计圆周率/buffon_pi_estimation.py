import numpy as np
import matplotlib.pyplot as plt

def buffon_needle(num_trials, needle_length=1.0, line_distance=1.0):
    hits = 0
    for _ in range(num_trials):
        # 针中心到最近线的距离
        y = np.random.uniform(0, line_distance / 2)
        # 针与平行线的夹角
        theta = np.random.uniform(0, np.pi / 2)
        # 是否与线相交
        if y <= (needle_length / 2) * np.sin(theta):
            hits += 1
    if hits == 0:
        return None  # 防止除零
    pi_estimate = (2 * needle_length * num_trials) / (hits * line_distance)
    return pi_estimate

if __name__ == "__main__":
    trials_list = [100, 1000, 10000, 100000]
    for trials in trials_list:
        pi_est = buffon_needle(trials)
        print(f"实验次数: {trials}, 估计的π值: {pi_est:.6f}, 误差: {abs(np.pi - pi_est):.6f}")
    
trials_list = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
pi_estimates = []

for trials in trials_list:
    pi_est = buffon_needle(trials)
    pi_estimates.append(pi_est)

plt.figure(figsize=(8,5))
plt.plot(trials_list, pi_estimates, marker='o', label='Estimated π')
plt.axhline(np.pi, color='r', linestyle='--', label='True π')
plt.xscale('log')
plt.xlabel('Number of Trials')
plt.ylabel('Estimated π')
plt.title('Buffon Needle Experiment: Estimated π vs. Number of Trials')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('buffon_pi_results.png')
plt.show()
