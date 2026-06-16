import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

mat_data = loadmat("test_resp.mat")
t = np.arange(0, 30, 0.05)
y = mat_data["y"].flatten()

Y = np.zeros_like(y)


def LMS(y, mu, M):
    W = np.zeros(M)
    U = np.zeros(M)
    E = 0
    Y[:M] = y[:M]
    W[M - 1] = 1
    for i in range(M, len(y)):
        U = y[i - M : i][::-1]
        Y[i] = W @ U
        E += (y[i] - Y[i]) ** 2
        W = W + mu * (y[i] - Y[i]) * U
    return Y, E


Ylms, RMSE = LMS(y, 0.003, 2)

RMSE = np.sqrt((RMSE) * 1 / len(Y))

plt.figure(figsize=(10, 5))
plt.plot(t, y, label="Original Signal", color="blue", alpha=0.6)
plt.plot(t, Ylms, label="LMS Filtered Output", color="red", linestyle="--")
plt.title(f"LMS Adaptive Filter Performance (RMSE: {RMSE:.4f})")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
