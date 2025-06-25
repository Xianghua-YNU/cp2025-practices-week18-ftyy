import numpy as np

# 1. 定义 p(x) = 1/(2√x) 的采样方法
def sample_from_p(N):
    u = np.random.rand(N)
    return u**2

# 2. 估计积分 I = ∫ f(x)/p(x) * p(x) dx
def importance_sampling_integral(N):
    x_samples = sample_from_p(N)
    f_samples = 2 / (np.exp(x_samples) + 1)  # f(x)/p(x)
    estimate = np.mean(f_samples)
    return estimate, f_samples

# 3. 误差估计
def estimate_error(f_samples, N):
    mean_f = np.mean(f_samples)
    mean_f2 = np.mean(f_samples**2)
    var_f = mean_f2 - mean_f**2
    sigma = np.sqrt(var_f / N)
    return sigma

# 4. 主程序
if __name__ == "__main__":
    N = 1_000_000
    I, f_samples = importance_sampling_integral(N)
    sigma = estimate_error(f_samples, N)

    print(f"积分估计值：{I:.6f}")
    print(f"统计误差：{sigma:.6f}")
