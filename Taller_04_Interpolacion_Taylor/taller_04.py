
import math
import numpy as np
import matplotlib.pyplot as plt

# PARTE B: Python basico

x = 0.5
suma = 0
termino = 1

for k in range(1, 4):
    suma = suma + termino
    termino = termino * x / k

print("Resultado:", suma)


# Metodo de Horner

def horner(coefs, x):
    p = 0
    for a in coefs:
        p = p * x + a
    return p

print("Horner 1:", horner([2, -3, 0, 1, -5], 2))
print("Horner 2:", horner([-5, 1, 0, -3, 2], 2))

print("Horner con arreglo:")
print(horner([2, -3, 0, 1, -5], np.linspace(0, 1, 5)))


# PARTE C: Polinomios de Taylor

def taylor_ln(x, n):
    suma = 0
    for k in range(1, n + 1):
        suma = suma + (-1)**(k + 1) * (x - 1)**k / k
    return suma


# Verificacion de resultados

print("P3(1.5):", round(taylor_ln(1.5, 3), 6))
print("P10(1.5):", round(taylor_ln(1.5, 10), 6))
print("P10(2.5):", round(taylor_ln(2.5, 10), 6))


# GRAFICA 1

x = np.linspace(0.1, 3, 400)

plt.figure()
plt.plot(x, np.log(x), label="ln(x)")
plt.plot(x, taylor_ln(x, 1), label="P1")
plt.plot(x, taylor_ln(x, 2), label="P2")
plt.plot(x, taylor_ln(x, 3), label="P3")
plt.plot(x, taylor_ln(x, 6), label="P6")

plt.scatter(1, 0, label="(1, 0)")
plt.ylim(-3, 2)
plt.title("Polinomios de Taylor de ln(x)")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.grid()
plt.savefig("grafica_1.png", dpi=200)


# GRAFICA 2

grados = np.arange(1, 31)

error_15 = []
error_25 = []
cota = []

for n in grados:
    error_15.append(abs(math.log(1.5) - taylor_ln(1.5, n)))
    error_25.append(abs(math.log(2.5) - taylor_ln(2.5, n)))
    cota.append(0.5**(n + 1) / (n + 1))

plt.figure()
plt.semilogy(grados, error_15, label="Error en x = 1.5")
plt.semilogy(grados, error_25, label="Error en x = 2.5")
plt.semilogy(grados, cota, "--", label="Cota del error")

plt.title("Error de los polinomios de Taylor")
plt.xlabel("Grado n")
plt.ylabel("Error absoluto")
plt.legend()
plt.grid()
plt.savefig("grafica_2.png", dpi=200)


# Menor grado con error inferior a 10^-6

for n in range(1, 31):
    error = abs(math.log(1.5) - taylor_ln(1.5, n))
    if error < 10**(-6):
        print("Menor grado:", n)
        break

plt.show()
