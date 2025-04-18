import numpy as np
import matplotlib.pyplot as plt

mu = 3
lambdas = np.arange(1, 2.9, 0.1)
Ws = []
Wqs = []
Ls = []

for lmbda in lambdas:
    metrics = mm1_metrics(lmbda, mu)
    Ws.append(metrics['W'])
    Wqs.append(metrics['Wq'])
    Ls.append(metrics['L'])

plt.figure(figsize=(10, 6))
plt.plot(lambdas, Ls, label='Среднее число заявок в системе (L)')
plt.plot(lambdas, Ws, label='Среднее время в системе (W)')
plt.plot(lambdas, Wqs, label='Время ожидания (Wq)')
plt.xlabel("Интенсивность λ")
plt.ylabel("Значение метрики")
plt.title("Поведение системы M/M/1 при разных λ")
plt.grid(True)
plt.legend()
plt.show()

def mm1_metrics(lmbda, mu):
    rho = lmbda / mu
    if rho >= 1:
        raise ValueError("Система нестабильна (λ ≥ μ)")
    L = rho / (1 - rho)
    W = 1 / (mu - lmbda)
    Wq = lmbda / (mu * (mu - lmbda))
    return {'ρ': rho, 'L': L, 'W': W, 'Wq': Wq}
