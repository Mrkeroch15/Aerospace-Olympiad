import math
import matplotlib.pyplot as plt

m = 5
k = 0.05
M3 = 2000
M2 = 30000
M1 = 80000
g = 9.81
U1 = 4000
MU1 = 300
CXS = 0.4 * 2/2
RE = 6371000
tau = 1
MK = M1 + M2 + M3 + m
FT = U1 * MU1
N = int(M1 * (1 - k)/(MU1 * tau))
V = 0
h = 0
i = 0
VL = []
hL = []
tL = []

while (i <= N):
    y = h/9000
    RO = 1.2/pow(0.367, y)
    FC = 0
    if (h <= 9000):
        FC = CXS * RO * V * V
        tAT = tau * i
    x = 1 + h / RE
    FG = g * MK/(x * x)
    F = FT - FG - FC
    VL.append(V)
    hL.append(h)
    t = tau * i
    tL.append(t)
    h = h + V * tau
    V = V + F * tau/MK
    MK = MK - MU1 * tau
    i += 1

print("R =", RE + h)
print("h =", h)
print("V =", V)
print("tAT =", tAT)
print("t =", t)

plt.figure()

plt.subplot(1, 2, 1)
plt.title('График траектории в осях. Изменение скорости от времени')
plt.xlabel('t')
plt.ylabel('V')
plt.plot(tL, VL)
plt.legend()

plt.subplot(1, 2, 2)
plt.title('График траектории в осях. Изменение высоты от времени')
plt.xlabel('t')
plt.ylabel('h')
plt.plot(tL, hL)
plt.legend()

plt.show()
