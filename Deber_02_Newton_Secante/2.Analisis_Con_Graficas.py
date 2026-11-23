

import numpy as np
import matplotlib.pyplot as plt

# Metodos numericos
def secante(f, p0, p1, tol=1e-6, max_iter=50):
    puntos = [p0, p1]

    for i in range(2, max_iter + 1):
        f0 = f(p0)
        f1 = f(p1)

        if abs(f1 - f0) < 1e-14:
            break

        p2 = p1 - f1 * (p1 - p0) / (f1 - f0)
        puntos.append(p2)

        if abs(p2 - p1) < tol:
            break

        p0, p1 = p1, p2

    return puntos


def newton_raphson(f, df, p0, tol=1e-6, max_iter=50):
    puntos = [p0]

    for i in range(max_iter):
        if abs(df(p0)) < 1e-14:
            break

        p1 = p0 - f(p0) / df(p0)
        puntos.append(p1)

        if abs(p1 - p0) < tol:
            break

        p0 = p1

    return puntos


# Ejercicio 1
def P(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9


def dP(x):
    return 920*x**3 + 54*x**2 + 18*x - 221


# Calculo con la secante
aproximaciones = secante(P, 0, 1)
raiz_negativa = aproximaciones[-1]
raiz_positiva = secante(P, 0.9, 1)[-1]

# Calculo con Newton
newton_medio = newton_raphson(P, dP, 0.5)[-1]
newton_positivo = newton_raphson(P, dP, 0.9)[-1]

print("EJERCICIO 1")
print("Metodo de la secante:")

for i, p in enumerate(aproximaciones):
    print(f"p{i} = {p:.9f}")

print(f"Secante desde 0 y 1 = {raiz_negativa:.12f}")
print(f"Newton desde 0.5 = {newton_medio:.12f}")
print(f"Raiz negativa = {raiz_negativa:.12f}")
print(f"Raiz positiva = {raiz_positiva:.12f}")
print(f"Newton desde 0.9 = {newton_positivo:.12f}")


# Grafica del ejercicio 1
x = np.linspace(-1.4, 1.1, 1000)
y = P(x)

plt.figure(figsize=(11, 6))
plt.plot(x, y, color="blue", label="P(x)")
plt.axhline(0, color="black", linewidth=1)

# Raices
for r in [raiz_negativa, raiz_positiva]:
    plt.plot(r, 0, "go", markersize=8)
    plt.annotate(
        f"Raiz: {r:.6f}",
        (r, 0),
        xytext=(0, 35),
        textcoords="offset points",
        ha="center",
        color="green"
    )

# Aproximaciones p0 a p4
for i, p in enumerate(aproximaciones[:5]):
    plt.plot(p, 0, "ro", markersize=5)
    plt.annotate(
        f"p{i}",
        (p, 0),
        xytext=(0, -18 - (i % 2)*17),
        textcoords="offset points",
        ha="center",
        color="red"
    )

plt.xlim(-1.4, 1.1)
plt.ylim(-250, 250)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title(r"$P(x)=230x^4+18x^3+9x^2-221x-9$")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("Ejercicio_1_Polinomio.png", dpi=300)


# Ejercicio 2
def f(x):
    return np.log(x**2 + 1) - np.exp(0.4*x)*np.cos(np.pi*x)


# Grafica del ejercicio 2
x2 = np.linspace(-1, 5, 1500)
y2 = f(x2)

plt.figure(figsize=(11, 6))
plt.plot(x2, y2, color="blue", label="f(x)")
plt.axhline(0, color="black", linewidth=1)

plt.xlim(-1, 5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(r"$f(x)=\ln(x^2+1)-e^{0.4x}\cos(\pi x)$")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("Ejercicio_2_Ceros_Funcion.png", dpi=300)


# Calculo del cero positivo numero 25
puntos = secante(f, 24.4, 24.6)
raiz25 = puntos[-1]

print("\nEJERCICIO 2")
print(f"Cero positivo 25 = {raiz25:.12f}")

plt.show()
