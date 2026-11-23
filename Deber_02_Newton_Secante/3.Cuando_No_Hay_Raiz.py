
import numpy as np

# Primer ejercicio
def f(x):
    return np.exp(x)

def df(x):
    return np.exp(x)

# Metodo de Newton-Raphson
def newton_raphson(f, df, p0, tol=1e-6, n0=50):
    for i in range(1, n0 + 1):
        p = p0 - f(p0) / df(p0)

        if i == 50:
            print(f"p50 = {p:.6f}")

        if abs(p - p0) < tol:
            return p

        p0 = p

    raise RuntimeError("Se agotaron las 50 iteraciones")


# Resultado del primer ejercicio
try:
    newton_raphson(f, df, 0)
except RuntimeError as error:
    print(error)


# Newton con criterio del residuo
def newton_residuo(f, df, p0, tol=1e-6, n0=50):
    for i in range(1, n0 + 1):
        p = p0 - f(p0) / df(p0)

        if abs(f(p)) < tol:
            return p

        p0 = p

    raise RuntimeError("Se agotaron las iteraciones")

resultado = newton_residuo(f, df, 0)
print(f"Resultado con residuo = {resultado:.6f}")


import matplotlib.pyplot as plt

# Segundo ejercicio
def s(t):
    return np.exp(-t/2) * (1.2 + np.cos(2*t))

t = np.linspace(0, 12, 1000)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Grafica de s(t)
ax[0].plot(t, s(t), color="blue")
ax[0].axhline(0, color="black")
ax[0].set_title(r"$s(t)=e^{-t/2}(1.2+\cos(2t))$")
ax[0].set_xlabel("t")
ax[0].set_ylabel("s(t)")
ax[0].grid(True)

# Grafica sin el factor exponencial
ax[1].plot(t, 1.2 + np.cos(2*t), color="green")
ax[1].axhline(0.2, color="red", linestyle="--", label="y = 0.2")
ax[1].set_title(r"$s(t)e^{t/2}=1.2+\cos(2t)$")
ax[1].set_xlabel("t")
ax[1].set_ylabel("s(t)e^(t/2)")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.savefig("Ejercicio_3_Senal_Sensor.png", dpi=300)
plt.show()


# Tercer ejercicio - SciPy
from scipy.optimize import newton

raiz, info = newton(
    np.exp, 0,
    fprime=np.exp,
    maxiter=1000,
    full_output=True
)

print("\nEJERCICIO 3 - SCIPY")
print(f"Raiz = {raiz}")
print(f"Convergencia = {info.converged}")
print(f"f(raiz) = {np.exp(raiz)}")
