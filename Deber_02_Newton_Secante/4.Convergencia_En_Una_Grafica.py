
import numpy as np
import matplotlib.pyplot as plt
from metodos import biseccion, newton_raphson, secante

# Funcion del ejercicio
def f(x):
    return 3*x - np.exp(x)

def df(x):
    return 3 - np.exp(x)

# Aproximaciones de los tres metodos
puntos_biseccion = biseccion(f, 1, 2, 30)
puntos_newton = newton_raphson(f, df, 1.5, tol=1e-14)
puntos_secante = secante(f, 1, 2, tol=1e-14)

# Raiz de referencia
raiz = puntos_secante[-1]

print("SECCION 4 - CONVERGENCIA")
print(f"Raiz = {raiz:.15f}")
print(f"f(raiz) = {f(raiz):.15e}")

# Calculo de los errores
def calcular_errores(puntos, raiz):
    errores = []

    for p in puntos:
        error = abs(p - raiz)

        if error == 0:
            errores.append(np.nan)
        else:
            errores.append(error)

    return errores

errores_b = calcular_errores(puntos_biseccion, raiz)
errores_n = calcular_errores(puntos_newton, raiz)
errores_s = calcular_errores(puntos_secante, raiz)

# Numero de iteraciones
n_b = np.arange(1, len(puntos_biseccion) + 1)
n_n = np.arange(len(puntos_newton))
n_s = np.arange(len(puntos_secante))

# Cota de la biseccion
cota = (2 - 1) / (2.0 ** n_b)

# Grafica de convergencia
plt.figure(figsize=(11, 7))

plt.semilogy(n_b, errores_b, "o-",
             label="Biseccion", markersize=5)

plt.semilogy(n_n, errores_n, "s-",
             label="Newton-Raphson", markersize=5)

plt.semilogy(n_s, errores_s, "^-",
             label="Secante", markersize=5)

plt.semilogy(n_b, cota, "--",
             label="Cota de biseccion")

plt.axhline(1e-8, color="red", linestyle=":",
            label="Tolerancia 1e-8")

plt.xlabel("Iteracion n")
plt.ylabel("Error absoluto |pn - p|")
plt.title(r"Convergencia de los metodos: $3x-e^x=0$")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Guardar la grafica
plt.savefig("Ejercicio_4_Convergencia.png", dpi=300)

plt.show()

# Resultados
print("\nIteraciones realizadas:")
print(f"Biseccion: {len(puntos_biseccion)}")
print(f"Newton: {len(puntos_newton)-1}")
print(f"Secante: {len(puntos_secante)-2}")
