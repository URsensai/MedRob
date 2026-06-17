import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

mat_data = loadmat("test_resp.mat")
y = mat_data["y"].flatten()
t = np.arange(0, len(y) * 0.05, 0.05)[: len(y)]


def LMS_handout(y, mu, M):
    n_total = len(y)
    Ylms = np.zeros(n_total)
    E = np.zeros(n_total)

    w = np.zeros(M)
    w[-1] = 1.0
    Ylms[:M] = y[:M]  # Initial condition: y_hat = y_1

    for n in range(M - 1, n_total - 1):
        # Slice matches 1-based index: y(n-M+1 : n)
        u = y[n - M + 1 : n + 1]

        Ylms[n + 1] = np.dot(w, u)
        E[n] = y[n] - Ylms[n]
        w = w + mu * E[n] * u

    E[-1] = y[-1] - Ylms[-1]
    return Ylms, E


# Configuration Grid
M_vals = [2, 4, 8]
mu_vals = [0.0005, 0.001, 0.005]
RMSE = np.zeros([len(M_vals), len(mu_vals)])

# Execution and Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, y, label="Original Respiration Signal", color="black", alpha=0.5)

for i, M in enumerate(M_vals):
    for j, mu in enumerate(mu_vals):
        Ylms, E = LMS_handout(y, mu, M)
        # Calculate RMS excluding the initial initialization window
        RMSE[i, j] = np.sqrt(np.mean(E[M:] ** 2))

        if mu == 0.001:  # Plot the requested hint values for clarity
            plt.plot(t, Ylms, label=f"Predicted (M={M}, $\mu$={mu})", linestyle="--")

print("Handout Formula RMSE Matrix:")
print(RMSE)

plt.title("Respiration Signal Prediction Comparison (Handout LMS)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
