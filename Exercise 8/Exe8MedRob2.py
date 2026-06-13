import numpy as np

Y = np.array([1 / np.sqrt(2), 1, 1 / np.sqrt(2), 0])
W = np.zeros(4)
Ylms = np.zeros(4)
E = np.zeros(4)

W[0] = 1.0
mu = 0.1

for i in range(0, 3):
    Ylms[i] = W[i] * Y[i]
    E[i] = Y[i] - Ylms[i]
    W[i + 1] = W[i] + mu * E[i] * Y[i]

y4_pred = W[3] * Y[3]

print(f"Weights sequence: {W}")
print(f"Prediction for y4: {y4_pred}")
