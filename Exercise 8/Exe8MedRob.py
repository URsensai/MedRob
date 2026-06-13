import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 30, 0.05)
P = np.sin(t + 0.2014)

R = np.zeros(len(P))

for i in range(1, len(P)):
    R[i] = P[i - 1]


def MULIN0(P, R):
    Pt = np.zeros(len(P))
    RMSE = 0
    for i in range(len(P)):
        Pt[i] = P[i] + (P[i] - R[i])

        RMSE = RMSE + (P[i] - Pt[i]) ** 2
    return Pt, RMSE


def MULIN1(P, R):
    Pt = np.zeros(len(P))
    Pt[0] = P[0]
    RMSE = 0
    for i in range(1, len(P)):
        Pt[i] = P[i] + 2 * (P[i] - R[i]) - (P[i - 1] - R[i - 1])
        RMSE = RMSE + (P[i] - Pt[i]) ** 2
    return Pt, RMSE


def MULIN2(P, R):
    Pt = np.zeros(len(P))
    Pt[0] = P[0]
    Pt[1] = P[1]
    RMSE = 0
    for i in range(2, len(P)):
        Pt[i] = (
            P[i] + 4 * (P[i] - R[i]) - 4 * (P[i - 1] - R[i - 1]) + (P[i - 2] - R[i - 2])
        )
        RMSE = RMSE + (P[i] - Pt[i]) ** 2
    return Pt, RMSE


P0t, RMSE0 = MULIN0(P, R)
P1t, RMSE1 = MULIN1(P, R)
P2t, RMSE2 = MULIN2(P, R)

E0 = P0t - P
E1 = P1t - P
E2 = P2t - P

RMSE0 = np.sqrt(RMSE0 / len(P))
RMSE1 = np.sqrt(RMSE1 / len(P))
RMSE2 = np.sqrt(RMSE2 / len(P))

print(f"RMSE0: {RMSE0:.6f}")
print(f"RMSE1: {RMSE1:.6f}")
print(f"RMSE1: {RMSE2:.6f}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot predictions
ax1.plot(t, P, label="Actual", color="k")
ax1.plot(t, P0t, label="MULIN0", linestyle=":")
ax1.plot(t, P1t, label="MULIN1", linestyle=":")
ax1.plot(t, P2t, label="MULIN2", linestyle=":")
ax1.set_title("Prediction Comparison")
ax1.legend()

# Plot errors
ax2.plot(t, E0, label="Err0")
ax2.plot(t, E1, label="Err1")
ax2.plot(t, E2, label="Err2")
ax2.set_title("Error Comparison")
ax2.legend()
plt.tight_layout()
plt.show()
