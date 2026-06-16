import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2, 0.05)
P = np.sin(t + 0.2014)


def MULIN0(P):
    p = np.zeros(len(P))
    p[0] = P[0]
    p[1] = P[1]
    for j in range(1, len(P) - 1):
        p[j + 1] = 2 * P[j] - P[j - 1]
    return p


def MULIN1(P):
    p = np.zeros(len(P))
    # Warm-up assignments
    p[0], p[1], p[2] = P[0], P[1], P[2]

    for j in range(2, len(P) - 1):
        p[j + 1] = 3 * P[j] - 3 * P[j - 1] + P[j - 2]
    return p


def MULIN2(P):
    p = np.zeros(len(P))
    # Warm-up assignments
    p[0], p[1], p[2], p[3] = P[0], P[1], P[2], P[3]

    for j in range(3, len(P) - 1):
        p[j + 1] = 5 * P[j] - 8 * P[j - 1] + 5 * P[j - 2] - P[j - 3]
    return p


p0 = MULIN0(P)
p1 = MULIN1(P)
p2 = MULIN2(P)

print(P)
print(p2)

E0 = np.sqrt(np.mean((P - p0) ** 2))
E1 = np.sqrt(np.mean((P - p1) ** 2))
E2 = np.sqrt(np.mean((P - p2) ** 2))

print(E0)
print(E1)
print(E2)
